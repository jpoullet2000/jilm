import pytest
from pathlib import Path

current_folder = Path(__file__).parent

@pytest.fixture(scope="session")
def data_folder():
    return current_folder / "data"

@pytest.fixture(scope="session")
def csv_file(data_folder):
    return data_folder / "auto-mpg.csv"

