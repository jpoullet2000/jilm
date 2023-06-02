"""Settings for jilm project."""
import os
from pygptj.model import Model

from dotenv import load_dotenv
from chromadb.config import Settings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms.openai import OpenAI

load_dotenv()

# Define the folder for storing database
PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY')

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
        chroma_db_impl='duckdb+parquet',
        persist_directory=PERSIST_DIRECTORY,
        anonymized_telemetry=False
)

# Define the LLM model
def get_gpt4all_model():
    """Return the GPT4ALL model."""
    llm_model_path = os.getenv("JILM_LLM_MODEL_PATH")
    if llm_model_path is None:
        raise ValueError("JILM_LLM_MODEL environment variable not set")
    return Model(llm_model_path)

def get_gpt4_model():
    """Return the GPT4 model."""
    return OpenAI


def pick_model():
    """Pick the model based on the MODEL_TYPE environment variable.

    Raises:
        ValueError: Model type not set

    Returns:
        Model: The LLM model
    """
    if os.environ.get('MODEL_TYPE') == "GPT4All":
        return get_gpt4all_model()
    elif os.environ.get('MODEL_TYPE') == "GPT4":
        return get_gpt4_model()
    else:
        raise ValueError("MODEL_TYPE environment variable not set")

llm_model = pick_model()
llm_type = os.environ.get("MODEL_TYPE")

# Embeddings
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME')
embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)

