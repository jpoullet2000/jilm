from jilm.settings import get_chroma_settings
import jilm
PERSIST_DIRECTORY="tmp/vector-db"


def test_get_chroma_settings(mocker):
    mocker.patch('jilm.settings.Settings', return_value='mocked_chroma_settings')
    get_chroma_settings()
    jilm.settings.Settings.assert_called_once_with(
        chroma_db_impl='duckdb+parquet',
        persist_directory=PERSIST_DIRECTORY,
        anonymized_telemetry=False
    )
