import streamlit as st
from src.prompting_text_to_sql import main as handle_question_with_prompt
from app._pages.utils import *


c1, c2 = st.columns([5, 5])

init_values("final_response", "")
init_values("question", "")
init_values("sql", "")
init_values("df", None)


with c1:
    question = st.text_area("Your Question:", key="input", height=100)
    col1, col2, _ = st.columns([5, 5, 21], vertical_alignment="top")
    with col1:
        question_button = st.button("Ask a question")
    with col2:
        random_button = st.button("Random question")

    if random_button:
        question = random_question()

    if question_button or random_button:
        if validate_question(question):
            st.session_state.question = question
            st.session_state.sql, st.session_state.df, st.session_state.final_response, retrying, question_with_error = (
                handle_question_with_prompt(question)
            )

            if st.session_state.sql.startswith(("INSERT", "UPDATE", "DELETE")):
                # STILL UNDER DEVELOPMENT
                st.warning("You are not allowing to manipulate the database.")
            else:
                if retrying:
                    st.info("Retrying with additional context...")
                    if question_with_error:
                        with st.expander("AI response (SQL query)", expanded=False):
                            with st.chat_message("ai"):
                                st.code(st.session_state.sql, language="sql")
                            with st.chat_message("user"):
                                st.write(f"{question_with_error}")

                
    if st.session_state.sql:
        st.markdown("##### AI response (SQL query)")
        st.code(st.session_state.sql, language="sql")
    if st.session_state.df is not None:
        st.markdown("##### SQL response (Query results)")
        st.dataframe(st.session_state.df)
        
with c2:
    with st.expander("AdventureWorks Schema"):
        st.image("data/database/adventureworks_schema.png")
    with st.expander("Prompting framework"):
        st.image("app/ui/static/prompt-engineering.gif")

    if st.session_state.final_response:
        st.markdown("##### Final LLM Answer")
        with st.chat_message("ai"):
            st.write(st.session_state.final_response)
