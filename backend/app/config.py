import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/sitesage"
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")