from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Project root path
PROJ_ROOT = Path(__file__).resolve().parents[1]

# ==========================
#         DATASETS
# ==========================

RAW_DATA = PROJ_ROOT / "data/raw"

# ==========================
#         DATABASE
# ==========================

DATABASE_DIR = PROJ_ROOT / "data/database/adventureworks.db"

DB_URL = f"sqlite:///{DATABASE_DIR}"

DATABASE_SCHEMA = PROJ_ROOT / "data/database/schema.sql"

DB_CONFIG = {
    "host": "xxx.x.x.x",
    "user": "xxxx",
    "password": "xxxxxxxxxxxxxx",
    "database": "adventureworks",
    "port": 3306
}

IMAGE_PROMPT_PATH = PROJ_ROOT / "data/database/adventureworks_schema.png"

# ==========================
#         MODELS
# ==========================

MODEL_NAME = "models/gemini-1.5-flash"
EMBEDDING_MODEL = "models/embedding-001"  # | 'models/embedding-gecko-001' | 'models/text-embedding-004' | paper @ https://arxiv.org/pdf/2403.20327 # https://ai.google.dev/models/gemini#embedding

# ==========================
#         SECRETS
# ==========================

# API KEY
# NOTE: when running locally, you can load Google Gemini API key from environment variables (.env file)
# To get API Key, create free one from here : https://aistudio.google.com/app/apikey

# To run locally, uncomment those lines
# import os
# API_KEY = os.getenv("GOOGLE_API_KEY")

API_KEY = st.secrets["GOOGLE_API_KEY"]