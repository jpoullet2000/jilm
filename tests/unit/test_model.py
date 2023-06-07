# pylint: disable=missing-docstring
def test_build_model(build_model_results):
    """Test build_model."""
    from jilm.model import build_model # necessary to import here to be mocked
    res = build_model(callbacks=[...])
    build_model.assert_called_once_with(callbacks=[...])
    assert res is not None
    assert res == 'mocked_llm_model'
