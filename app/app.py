import streamlit as st
import PIL.Image as PIL
from st_pages import add_page_title, get_nav_from_toml


def intro():
    """Main Home page intro"""
    st.header("**Welcome to the AdventureWorks-Database!**")
    with st.expander("About the app"):
        st.info(
            "- This app uses Google [Gemini Flash](https://developers.googleblog.com/en/gemini-15-flash-8b-is-now-generally-available-for-use/) to convert natural language questions into SQL queries.  \n"
            "- The **Prompt Engineering** method leverages a model trained with the database schema and ERD to ensure accurate query generation.  \n"
            "- The **RAG** method enhances query accuracy by retrieving relevant context from a database before generating responses.  \n"
        )
        st.success(
            "- The app executes the generated SQL queries on a SQLite3 database and displays both the queries and the results.  \n"
            "- If an error occurs during execution, the app automatically resubmits the original question along with the error message for improved accuracy.  \n"
            "- You can explore the database structure to formulate relevant questions or click 'Random Questions'"
        )


def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Test to SQL Generator — by Ahmed Salim",
        page_icon=PIL.open("app/ui/static/favicon.ico"),
        layout="wide",
    )
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    intro()

    rag = True
    nav = get_nav_from_toml(
        "app/.streamlit/pages_sections.toml" if rag else "app/.streamlit/pages.toml"
    )

    st.logo("app/ui/static/favicon.ico")

    pg = st.navigation(nav)

    add_page_title(pg)

    pg.run()

    st.markdown("</div>", unsafe_allow_html=True)
    with open("app/ui/footer.html", "r", encoding="utf-8") as f:
        footer_content = f.read()
    st.markdown(footer_content, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
