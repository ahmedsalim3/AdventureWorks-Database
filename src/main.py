from src.prompting_text_to_sql import main as handle_question_with_prompt
from src.rag_text_to_sql import main as handle_question_with_rag


if __name__ == "__main__":
    
    # Provide your question
    question = "Provide a breakdown of total sales quantities by region and country for each year from 2015 to 2017, from highest to lowest"
    
    # Run with prompting approach
    sql, df, final_answer, retry, question_with_error = handle_question_with_prompt(question)
    print(f'\n\n:===================Final Answer:===================\n\n{final_answer}')
    
    # Run with RAG approach
    # retrieval, sql, df, final_answer, retrying, question_with_error = handle_question_with_rag(question)
    # print(f'\n\n:===================Final Answer:===================\n\n{final_answer}')
