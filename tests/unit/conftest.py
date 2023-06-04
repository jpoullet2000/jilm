"""Conftest for unit tests."""
import pytest
from pathlib import Path
import pytest

current_folder = Path(__file__).parent

@pytest.fixture
def my_fixture(mocker):
    """Mock the AI assistant."""
    mocker.patch('jilm.model.build_model', return_value='mocked_value')
    return 'fixture_value'

@pytest.fixture(scope="session")
def data_folder():
    """Return the data folder."""
    return current_folder.parent / "data"

@pytest.fixture(scope="session")
def csv_file(data_folder):
    """Return the path to the auto-mpg.csv file."""
    return data_folder / "auto-mpg.csv"

