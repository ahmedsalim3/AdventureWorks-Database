import streamlit as st
import sqlite3
import google.generativeai as genai
import pandas as pd
from config import *
import random
import PIL.Image as PIL

# Load the API key from streamlit secrets
genai.configure(api_key=API_KEY)


def intro():
    """Main Home page intro"""
    st.header("**Welcome to the AdventureWorks-Database!**")
    with st.expander("About the app"):
        st.info(
            "- This app uses Google [Gemini Flash](https://developers.googleblog.com/en/gemini-15-flash-8b-is-now-generally-available-for-use/) to convert natural language questions into SQL queries.  \n"
            "- The model was prompted with a snapshot of the ERD and a text of database structure via [generate-content](https://github.com/google-gemini/generative-ai-python/blob/7546026dcad2bed72b181845ed93451bbefd2120/google/generativeai/generative_models.py#L237) from [generative-ai](https://github.com/google/generative-ai-docs).  \n"
        )
        st.success(
            "- The model's response is executed on the SQLite3 database, displaying both the SQL query and the results.  \n"
            "- If an error occurs during execution, the app automatically resubmits the original question along with the error message to the model for a more accurate query. \n"
            "- You can view the database structure to ask a relevant question or simply run 'Generate Random Questions'."
        )


def get_gemini_response(question):
    """Generate SQL queries as response from Google Gemini model"""
    # Text prompting: https://ai.google.dev/gemini-api/docs/prompting-intro
    # Media Prompting: https://ai.google.dev/gemini-api/docs/prompting_with_media?lang=python
    img = PIL.open(IMAGE_PROMPT)
    model = genai.GenerativeModel(
        model_name=MODEL_NAME, system_instruction=SYSTEM_INSTRUCTION
    )
    res = model.generate_content([TEXT_PROMPT, question, img])
    return res.text


def read_sql_query(sql, db):
    """Execute SQL query and retrieve results from the database"""
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        col_names = [desc[0] for desc in cur.description]
        # conn.commit()
        # conn.close()
        return rows, col_names, False
    except sqlite3.Error as e:
        return [], [], str(e)
    finally:
        if conn:
            conn.close()


def get_sql_response(ai_response):
    """Get the SQL response and display results."""
    cleaned_sql = ai_response.strip().strip("```").strip().strip("sql").strip()
    st.markdown("##### AI response (SQL query)")
    st.code(cleaned_sql, language="sql")

    sql_response, col_names, error = read_sql_query(cleaned_sql, DATABASE_DIR)

    # Check if the SQL query is a data manipulation query
    if ai_response.strip().lower().startswith(("insert", "update", "delete")):
        # STILL UNDER DEVELOPMENT
        st.success("Query execution successful.")

    if error is False:
        st.markdown("##### SQL response (Query results)")
        if len(sql_response) > 0:
            table_data = [col_names] + list(sql_response)
            df = pd.DataFrame(table_data[1:], columns=table_data[0])
            st.dataframe(df)
        else:
            st.warning("No results returned.")
    else:
        st.error(f"Error executing SQL query: {str(error)}")
        st.info("Retrying with additional context...")
        print(f"Quesion: {st.session_state.question}\nError{str(error)}")
        handle_question_submission(st.session_state.question, str(error))


def handle_question_submission(question, error_message=None):
    """Handle the question submission and display results"""
    if not question:
        st.warning("Please write a question, or submit a random question.")
        return

    question_prompt = (
        f"{question} (Previous error: {error_message})" if error_message else question
    )
    print(f"Question Prompt: {question_prompt}")
    ai_response = get_gemini_response(question_prompt)
    get_sql_response(ai_response)


def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Test to SQL Generator — by Ahmed Salim",
        page_icon=PIL.open("app/ui/favicon.ico"),
    )

    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    intro()

    if "question" not in st.session_state:
        st.session_state.question = ""

    question = st.text_area("Your Question:", key="input", height=100)

    col1, col2, _ = st.columns([5, 5.5, 13], vertical_alignment="top")
    with col1:
        question_button = st.button("Ask a question")
    with col2:
        random_button = st.button("Random question")

    if random_button:
        question = random.choice(random_questions)
        st.session_state.question = question
        st.markdown(question)

    if question_button or random_button:
        st.session_state.question = question
        handle_question_submission(question)

    st.markdown("</div>", unsafe_allow_html=True)

    with open("app/ui/footer.html", "r", encoding="utf-8") as f:
        footer_content = f.read()
    st.markdown(footer_content, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
