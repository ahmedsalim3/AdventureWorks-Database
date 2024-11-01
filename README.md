# Adventureworks Database

This repository provides a framework for setting up a relational MySQL database using Python, as well as building a Text-to-SQL Streamlit app that converts plain language questions into SQL queries. The application interacts with a SQLite database populated with AdventureWorks sample data.

Two approaches are used: **Prompt Engineering** and **Retrieval-Augmented Generation (RAG)**. Both utilize the same LLM, [**Gemini 1.5 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-1.5-flash), via [Google AI Studio](https://aistudio.google.com/app/prompts/new_chat?model=gemini-1.5-flash) to execute SQL queries on the database and retrieve results. For more details, see the publication.

<p align="center">
<img src="https://img.shields.io/badge/PYTHON-3.12-orange">
</p>

<div align="center">
    
[[`Publication`](https://app.readytensor.ai/publications/unlocking_sql_converting_natural_language_into_query_results_with_generative_ai_hrWFsOxy9Yfy)] [[`Dataset`](https://www.kaggle.com/datasets/ukveteran/adventure-works)] [[`Schema`](./data/database/adventureworks_schema.png)] [[`Streamlit App`](https://sql-unlocked.streamlit.app/)]

<div style="display: flex; justify-content: space-around;">
    <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/126220185/381777368-ad60713e-2f5c-4d1b-844d-22dca4a01581.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241031%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241031T035159Z&X-Amz-Expires=300&X-Amz-Signature=9c2c44cd30d3af81d279df9a17bd1b806490f8c8c2d2cbfa728331f73ad7561f&X-Amz-SignedHeaders=host" alt="Prompt Engineering">
</div>

</div>

## Installation

1. **Clone this repository:**

  ```bash
  git clone https://github.com/ahmedsalim3/AdventureWorks-Database.git
  ```

2. **Navigate to the repository directory:**

  ```bash
  cd AdventureWorks-Database
  ```

3. **Create a Virtual Environment (Recommended):**

  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

4. **Install Requirements:**

  ```bash
  pip install -r requirements.txt
  ```

## Create Database

1. Configure the database at [config](./src/config.py#L26-L32)

2. run `MySQLDatabaseManager` class to create the database, follow [TODO](./src/rdbms/TODO.md) file for more details

  ```bash
  cd rdbms
  python3 -m src.rdbms.csv2mysql
  ```
  
3. To explore the database tables run:

  ```bash
  python3 -m src.rdbms.table_info
  ```

## Run the App

Get yor API KEY, and set it in [config](./src/config.py#L47-L55):

  ```bash
  python3 -m streamlit run app/app.py
  ```

## Run the app via Dockerfile

  ```
  docker build -t image_name .

  docker run -p 8501:8501 image_name
  ```

## Repo's directory structure

```sh
.
├── app                          <- Streamlit related fils
│   ├── _pages                  
│   │   ├── prompt_page.py       <- Prompting app page
│   │   ├── rag_page.py          <- RAG app page
│   │   └── utils.py       
│   └── ui                       <- User interface components
│
├── data                         <- Data directory containing databases and raw data
│   ├── database
│   └── raw
│
└── src     
│   ├── rag
│   │   ├── documents.py          <- Document handling for RAG
│   │   ├── example               <- Vector database example
│   │   └── vector_db.py          <- sqlite-vec database
│   │
│   ├── rdbms                     <- Relational Database Management System tools
│   │   ├── TODO.md
│   │   ├── csv2mysql.py          <- Module for converting CSV to MySQL
│   │   ├── mysql2sqlite          <- Submodule for converting MySQL to SQLite
│   │   └── table_info.py
│   │
│   ├── config.py                 <- Configuration settings for the project
│   ├── constants.py              <- Constant values related to AdventureWorks database
│   ├── main.py                   <- Main file to run which approach
│   ├── prompting_text_to_sql.py  <- Prompting implementation for text-to-SQL
│   ├── rag_text_to_sql.py        <- RAG implementation for text-to-SQL
│   └── utils.py
│
├── app.py                        <- Main Streamlit app
├── requirements.txt

```
