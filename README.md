<p align= "center">
<img src="https://img.shields.io/github/stars/amedsalim/Text-to-SQL-Generator?style=flat&color=orange"></a>
<img src="https://hits.sh/github.com/amedsalim/Text-to-SQL-Generator.svg?label=views&color=orange"></a>
<img src="https://img.shields.io/badge/PYTHON-3.9-orange"></a>
<img src="https://img.shields.io/badge/Apache-2.0 license--3.0-orange"></a> 
</p>

<div align="center">
  
[[`Blog`](https://amedsalim.github.io/posts/Text-to-SQL)] [[`Dataset`](https://www.kaggle.com/datasets/ukveteran/adventure-works)] [`Schema`](https://amedsalim.github.io/assets/img/RDBMS/img1.png) [[`Demo App`](https://text-to-sql-generator.streamlit.app/)]
  
</div>

# Text-to-SQL App with Gemini Pro LLM

This repository contains a Streamlit application for generating and executing SQL queries using the Google Gemini API. The application interacts with a SQLite database populated with AdventureWorks sample data

## Features
- SQL Generation: Utilizes the Google Gemini API to translate natural language questions into SQL queries (SQLite)
- Database Connectivity: Executes generated SQL queries on the AdventureWorks SQLite database
- Streamlit Interface: Provides a user-friendly web interface for inputting questions and displaying query results

## Installation
1. **Clone this repository:**

```bash
git clone https://github.com/amedsalim/Text-to-SQL-Generator.git
```
2. **Navigate to the repository directory:**

```bash
cd Text-to-SQL-Generator
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
5. **Create a new [Gemini API](https://aistudio.google.com/app/apikey) and place it in a `.env` file:**
```bash
GOOGLE_API_KEY = 'Your API Key'
```

6. **Run the Streamlit application:**

```bash
streamlit run app.py
```
