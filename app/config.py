from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file if it exists
load_dotenv()

# Project root path
PROJ_ROOT = Path(__file__).resolve().parents[1]

# API KEY
# NOTE: when running locally, you can load Google Gemini API key from environment variables (.env file)
# To get API Key, create free one from here : https://aistudio.google.com/app/apikey

# To run locally, uncomment those lines
# import os
# API_KEY = os.getenv("GOOGLE_API_KEY")

API_KEY = st.secrets["GOOGLE_API_KEY"]

# Model configuration
MODEL_NAME = "models/gemini-1.5-flash"
IMAGE_PROMPT_PATH = PROJ_ROOT / "rdbms/adventureworks_schema.png"

# For rag
EMBEDDING_MODEL = "models/embedding-001"  # | 'models/embedding-gecko-001' | 'models/text-embedding-004' | paper @ https://arxiv.org/pdf/2403.20327 # https://ai.google.dev/models/gemini#embedding

# Database configuration
DATABASE_DIR = PROJ_ROOT / "rdbms/adventureworks.db"
DB_URL = f"sqlite:///{DATABASE_DIR}"

# DB_CONFIG = {
#     "host": "xxx.xxx.xx.xxx",
#     "user": "root",
#     "password": "xxxxxxxxx",
#     "database": "adventureworks",
#     "port": 3306
# }
