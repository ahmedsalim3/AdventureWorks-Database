# Text-to-SQL App with Gemini 1.5 Flash

This fle contains a Streamlit application for generating and executing SQL queries using the Google Gemini API. The application interacts with a SQLite database populated with AdventureWorks sample data

<p align= "center">
<img src="https://img.shields.io/badge/PYTHON-3.9+-orange">
</p>

<div align="center">
  
[[`Publication`](https://app.readytensor.ai/publications/unlocking_sql_converting_natural_language_into_query_results_with_generative_ai_hrWFsOxy9Yfy)] [[`Dataset`](https://www.kaggle.com/datasets/ukveteran/adventure-works)] [`Schema`](../rdbms/adventureworks_schema.png) [[`Streamlit App`](https://sql-unlocked.streamlit.app/)]
<div style="display: flex; justify-content: space-around;">
    <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/126220185/381777368-ad60713e-2f5c-4d1b-844d-22dca4a01581.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241031%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241031T035159Z&X-Amz-Expires=300&X-Amz-Signature=9c2c44cd30d3af81d279df9a17bd1b806490f8c8c2d2cbfa728331f73ad7561f&X-Amz-SignedHeaders=host" alt="Prompt Engineering">
</div>

</div>

## Features
- SQL Generation: Utilizes the Google Gemini API to translate natural language questions into SQL queries (SQLite)
- Database Connectivity: Executes generated SQL queries on the AdventureWorks SQLite database
- Streamlit Interface: Provides a user-friendly web interface for inputting questions and displaying query results

## Installation

1. **Clone this repository:**

  ```bash
  git clone https://github.com/ahmedsalim3/AdventureWorks-Database.git
  ```

2. **Navigate to the repository directory:**

  ```bash
  cd AdventureWorks-Database/app
  ```

3. **Create a Virtual Environment (Recommended):**

  ```bash
  python -m venv env
  .\env\Scripts\activate  # On Windows
  source env/bin/activate  # On macOS/Linux
  ```

4. **Install Requirements:**

  ```bash
  pip install -r requirements.txt
  ```

5. **Create a new [Gemini API](https://aistudio.google.com/app/apikey) and place it in a [config.py](https://github.com/ahmedsalim3/AdventureWorks-Database/blob/6b06f38f9c4a191edc41857312b4654617d6cfd3/app/config.py#L16) file:**

  ```bash
  API_KEY = os.getenv("GOOGLE_API_KEY")
  # comment this line as it's used for deployement, it access the api key through streamlit secrets
  # API_KEY = st.secrets["GOOGLE_API_KEY"]
  ```

6. **Run the Streamlit application:**

- From the [root](../) directory, run this:
    
    ```bash
    python -m streamlit run app/app.py
    ```

## Install via DockFile

    ```sh
    docker build -t image_name .

    docker run -p 8501:8501 image_name
    ```