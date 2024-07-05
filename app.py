# Copyright [2024] [Ahmed Salim] [https://amedsalim.github.io/]
# Read the article on the Streamlit app for SQL query generation @ [https://amedsalim.github.io/posts/Text-to-SQL]

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import sqlite3
from dotenv import load_dotenv
import os
import google.generativeai as gg
import pandas as pd
from constants import prompt, random_questions
import random

# Load Google Gemini API key from environment variables (.env file)
# To get API Key, create one from here : https://aistudio.google.com/app/apikey
load_dotenv()
gg.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    """
    Function to load Google Gemini Model and generate SQL queries as response
    """
    model=gg.GenerativeModel('gemini-pro')
    res=model.generate_content([prompt[0],question])
    return res.text

def read_sql_query(sql, db):
    """
    Function to execute SQL query and retrieve results from the database
    """
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        
        col_names = []
        for desc in cur.description:
            col_names.append(desc[0])
            
        conn.commit()
        conn.close()

        # debugging
        # for row in rows:
        #     print(row)
        
        return rows, col_names
    
    except sqlite3.Error as e:
        print(f"Error executing SQL query: {str(e)}")
        raise


st.set_page_config(page_title="Test to SQL Generator — by Ahmed Salim")

st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.header("AdventureWorks SQL Query Generator")

question = st.text_area("Your Question:", key="input", height=100)
question_button = st.button("Ask the question")
random_button = st.button("Generate Random Question")

if random_button:
    question = random.choice(random_questions)
    st.markdown(f'<p style="font-size: 14px; font-family: Arial, sans-serif; height: auto;">{question.upper()}</p>', unsafe_allow_html=True)

if question_button or random_button:
    if not question:
        st.warning("Please enter a question, or submit a Random Question.")
    else:
        # Generate SQL query using Gemini model
        ai_response = get_gemini_response(question, prompt)
        cleaned_sql = ai_response.strip().strip('```').strip().strip('sql').strip()

        # Display generated SQL query
        st.markdown("##### Generated SQL Query")
        st.code(cleaned_sql, language='sql')

        try:
            sql_response, col_names = read_sql_query(cleaned_sql, "adventureworks.db")

            st.markdown("##### Query Results")
            if len(sql_response) > 0:
                table_data = [col_names] + list(sql_response)
                df = pd.DataFrame(table_data[1:], columns=table_data[0])
                st.dataframe(df) 
            # Check if the SQL query is a data manipulation query
            if ai_response.strip().lower().startswith(("insert", "update", "delete")):
                st.success("Query execution successful.")
        except Exception as e:
            st.error(f"Error executing SQL query: {str(e)}")

st.markdown('</div>', unsafe_allow_html=True)

with open('./ui/footer.html', 'r', encoding='utf-8') as f:
    footer_content = f.read()
st.markdown(footer_content, unsafe_allow_html=True)