"""Conftest for unit tests."""
import pytest
from pathlib import Path
import os

current_folder = Path(__file__).parent
os.environ["MODEL_TYPE"] = "GPT4"

@pytest.fixture
def build_model_results(mocker):
    """Mock the AI assistant."""
    mocker.patch('jilm.model.build_model', return_value='mocked_llm_model')
    return 'mocked_value'

@pytest.fixture
def chroma_settings(mocker):
    """Create a Chroma settings object."""
    mocker.patch('chromadb.config.Settings', return_value='mocked_chroma_settings')
    return 'mocked_value'

@pytest.fixture(scope="session")
def data_folder():
    """Return the data folder."""
    return current_folder.parent / "data"

@pytest.fixture(scope="session")
def csv_file(data_folder):
    """Return the path to the auto-mpg.csv file."""
    return data_folder / "auto-mpg.csv"

