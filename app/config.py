from pathlib import Path
from dotenv import load_dotenv
from constants import prompt, random_questions
import streamlit as st

# Load environment variables from .env file if it exists
load_dotenv()

# Project root path
PROJ_ROOT = Path(__file__).resolve().parents[1]

# API KEY
# NOTE: when running locally, you can load Google Gemini API key from environment variables (.env file)
# To get API Key, create one from here : https://aistudio.google.com/app/apikey
# import os
# API_KEY = os.getenv("GOOGLE_API_KEY")
API_KEY = st.secrets["GOOGLE_API_KEY"]

# Model configuration
MODEL_NAME = "models/gemini-1.5-flash"
IMAGE_PROMPT = PROJ_ROOT / "rdbms/adventureworks_schema.png"
TEXT_PROMPT = prompt[0]  # Outputs the first string in the prompt list
SYSTEM_INSTRUCTION = [
    "You are an expert at translating English questions into SQL queries based on the AdventureWorks database described in the Schema Image, below",
    "Pay close attention to the table names and columns, as they are crucial for executing accurate SQL queries.",
]

# Database configuration
DATABASE_DIR = PROJ_ROOT / "rdbms/adventureworks.db"

# Additional configurations
RANDOM_QUESTIONS = random_questions
