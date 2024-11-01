import google.generativeai as genai
import pandas as pd
from src.config import API_KEY, DATABASE_DIR, MODEL_NAME, IMAGE_PROMPT_PATH
import PIL.Image as PIL
import logging
from src.constants import prompt
from src.utils import execute_sql_query, format_answer_prompt

logging.basicConfig(level=logging.INFO)

genai.configure(api_key=API_KEY)

SYSTEM_INSTRUCTION = [
    "You are an expert at translating natural language questions into SQL queries based on the AdventureWorks database described in the Schema Image, below.",
    "Pay close attention to the table names and columns, as they are crucial for executing accurate SQL queries.",
]

LLM = genai.GenerativeModel(model_name=MODEL_NAME, system_instruction=SYSTEM_INSTRUCTION)


def main(question):
    logging.info(f"Question: {question}")
    image_prompt = PIL.open(IMAGE_PROMPT_PATH)
    text_prompt = prompt[0]    
    
    res = LLM.generate_content([text_prompt, question, image_prompt])
    logging.info("Generating content using prompt engineering...")
    cleaned_sql = res.text.strip().strip("```").strip().strip("sqlite")
    logging.info(f'--LLM Responsed (SQL query)\n\n{cleaned_sql}')
    
    retry = False
    question_with_error = None
    
    if any(cmd in cleaned_sql.upper() for cmd in ["INSERT", "UPDATE", "DELETE"]):
        logging.warning("Data manipulation detected. Query not executed.")
        return cleaned_sql, None, "You are not allowed to manipulate the database.", retry, question_with_error

    rows, col_names, error = execute_sql_query(cleaned_sql, DATABASE_DIR)
    
    
    
    if error:
        logging.info('Retrying due to SQL error...')
        question_with_error = f'Dear this error caused: `{error}`\n{question}'
        logging.info(question_with_error)
        res = LLM.generate_content([text_prompt, question_with_error, image_prompt])
        
        cleaned_sql = res.text.strip().strip("```").strip().strip("sqlite")
        logging.info(cleaned_sql)
         
        rows, col_names, _ = execute_sql_query(cleaned_sql, DATABASE_DIR)
        retry = True

    if rows is not None:
        if not rows:  # If rows is empty
            return cleaned_sql, None, "No results found.", retry, question_with_error
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
        return cleaned_sql, df, final_response.text.strip(), retry, question_with_error

    return cleaned_sql, None, "No results found.", retry, question_with_error

        

# if __name__ == "__main__":
#     question = "Provide a breakdown of total sales quantities by region and country for each year from 2015 to 2017, from highest to lowest"
#     sql, df, final_answer, retry, question_with_error = main(question)
#     print(f'TEST:\n\n{final_answer}')
