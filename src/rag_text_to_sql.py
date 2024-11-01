import google.generativeai as genai
import pandas as pd
from src.config import API_KEY, DATABASE_DIR, MODEL_NAME
import logging
from src.rag.vector_db import VectorDatabase
from src.constants import schema_info
from src.utils import create_rag_prompt, execute_sql_query, format_answer_prompt

logging.basicConfig(level=logging.INFO)

genai.configure(api_key=API_KEY)

SYSTEM_INSTRUCTION = [
    "You are an expert SQL translator. Your primary task is to convert natural language questions into precise and optimized SQL queries. When given a question, follow these guidelines:",
    "1. **Identify the Intent**: Understand what the user is trying to achieve.",
    "2. **Date Functions**: Use SQLite-compatible date functions such as `strftime('%Y', OrderDate)` to extract components from dates.",
    "3. **Schema Awareness**: Familiarize yourself with the database schema, including primary and foreign keys.",
    "4. **Efficiency**: Aim for optimized queries, minimizing resource usage."
]

LLM = genai.GenerativeModel(model_name=MODEL_NAME, system_instruction=SYSTEM_INSTRUCTION)

def get_vector_db_retrieval(question, k=3):
    vec_db = VectorDatabase()
    vec_db.embed_sentences()
    return vec_db.retrieval(query=question, k=k)
    
def main(question, number_of_retrieval=3):
    logging.info(f"Question: {question}")
    retrieval = get_vector_db_retrieval(question, k=number_of_retrieval)
    top_k = 10 # number of lines to return
    
    rag_prompt = create_rag_prompt(number_of_retrieval, retrieval, schema_info, top_k)
    res = LLM.generate_content([rag_prompt, question])
    logging.info("Generating content using RAG prompt...")
    cleaned_sql = res.text.strip().strip("```").strip().strip("sqlite")
    logging.info(f'--LLM Responsed (SQL query)\n\n{cleaned_sql}')
    
    retry = False
    question_with_error = None
    
    if any(cmd in cleaned_sql.upper() for cmd in ["INSERT", "UPDATE", "DELETE"]):
        logging.warning("Data manipulation detected. Query not executed.")
        return retrieval, cleaned_sql, None, "You are not allowed to manipulate the database.", retry, question_with_error

    rows, col_names, error = execute_sql_query(cleaned_sql, DATABASE_DIR)
    
    if error:
        logging.info('Retrying due to SQL error...')
        question_with_error = f'Dear this error caused: `{error}`\n{question}'
        logging.info(question_with_error)
        
        res = LLM.generate_content([question_with_error, schema_info])
        cleaned_sql = res.text.strip().strip("```").strip().strip("sqlite")
        logging.info(cleaned_sql)
        
        rows, col_names, _ = execute_sql_query(cleaned_sql, DATABASE_DIR)
        retry = True

    if rows is not None:
        if not rows:
            return retrieval, cleaned_sql, None, "No results found.", retry, question_with_error
        
        # OPTION 1
        df = pd.DataFrame(rows, columns=col_names)
        logging.info(f'Results:\n{df}')
        # OPTION 2
        # if len(rows) > 0:
        #     table_data = [col_names] + list(rows)
        #     df = pd.DataFrame(table_data[1:], columns=table_data[0])
        #     logging.info(f'Results:\n{df}')
        
        if df.empty:
            result_summary = "The answer is 0."
        elif len(df) > 10:
            result_summary = f"The table explains df.head() results:\n{df.head()}"
        elif df.shape[0] == 1 and df.shape[1] == 1:  # single integer case
            result_summary = f'The answer is {df.iloc[0, 0]}'
        else:
            result_summary = df.to_string(index=False)

        # send to model using answer prompt
        answer = format_answer_prompt(question, cleaned_sql, result_summary)
        
        # final response
        final_response = LLM.generate_content([answer])
        logging.info(f"Model's final answer:\n{final_response.text.strip()}")
        
        return retrieval, cleaned_sql, df, final_response.text.strip(), retry, question_with_error

    return retrieval, cleaned_sql, None, "No results found.", retry, question_with_error
        

# if __name__ == "__main__":
#     question = "Provide a breakdown of total sales quantities by region and country for each year from 2015 to 2017, from highest to lowest"
#     retrieval, sql, df, final_response, retrying, question_with_error = main(question)
