"""Settings for jilm project."""
import os
from pygptj.model import Model

from dotenv import load_dotenv
from chromadb.config import Settings

load_dotenv()

# Define the folder for storing database
PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY')

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
        chroma_db_impl='duckdb+parquet',
        persist_directory=PERSIST_DIRECTORY,
        anonymized_telemetry=False
)

llm_model_path = os.getenv("JILM_LLM_MODEL_PATH")
if llm_model_path is None:
    raise ValueError("JILM_LLM_MODEL environment variable not set")

llm_model = Model(llm_model_path)
