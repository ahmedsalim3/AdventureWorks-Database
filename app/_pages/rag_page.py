import streamlit as st
from rag_text_to_sql import main as handle_question_with_rag
from _pages.utils import *


c1, c2 = st.columns([5, 5])

init_values("final_response_2", "")
init_values("retrieval", None)
init_values("sql_2", "")
init_values("df_2", None)
init_values("question_2", "")


def data_retrieved(retrieval):
    for i, _ in enumerate(retrieval):
        # index = retrieval[i][0]
        distance = retrieval[i][1]
        sentence = retrieval[i][2]
        table_name = retrieval[i][3]
        table_schema = retrieval[i][4]

        # return first retrieval data only
        if i == 0:
            return distance, sentence, table_name, table_schema


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
            st.session_state.question_2 = question
            (
                st.session_state.retrieval,
                st.session_state.sql_2,
                st.session_state.df_2,
                st.session_state.final_response_2,
                retrying,
                question_with_error,
            ) = handle_question_with_rag(question, number_of_retrieval=3)

            if st.session_state.sql_2.startswith(("INSERT", "UPDATE", "DELETE")):
                # STILL UNDER DEVELOPMENT
                st.warning("You are not allowing to manipulate the database.")
            else:
                if retrying:
                    st.info("Retrying with additional context...")
                    if question_with_error:

                        with st.expander("AI response (SQL query)", expanded=False):
                            with st.chat_message("ai"):
                                st.code(st.session_state.sql_2, language="sql")
                            with st.chat_message("user"):
                                st.write(f"{question_with_error}")

    if st.session_state.sql_2:
        st.markdown("##### AI response (SQL query)")
        st.code(st.session_state.sql_2, language="sql")
    if st.session_state.df_2 is not None:
        st.markdown("##### SQL response (Query results)")
        st.dataframe(st.session_state.df_2)


with c2:
    with st.expander("AdventureWorks Schema"):
        st.image("rdbms/adventureworks_schema.png")
    with st.expander("RAG framework"):
        st.image("app/ui/static/rag.gif")

    if st.session_state.final_response_2 and st.session_state.retrieval is not None:
        distance, sentence, table_name, table_schema = data_retrieved(
            st.session_state.retrieval
        )

        with st.expander(
            "View data retrieved from the vector database", expanded=False
        ):

            options = st.selectbox(
                label="Select an option",
                options=["Table", "Table Schema", "Sentence"],
            )

            if options == "Table":
                st.markdown(
                    f"The first table retrieved is **`{table_name}`** with a distance of **`{distance}`**"
                )
            if options == "Sentence":
                st.info(sentence)
            elif options == "Table Schema":
                st.code(table_schema, language="sql")

        st.markdown("##### Final LLM Answer")
        with st.chat_message("ai"):
            st.write(st.session_state.final_response_2)
