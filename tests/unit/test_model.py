def test_build_model(build_model_results):
    """Test build_model."""
    from jilm.model import build_model
    res = build_model()
    assert res is not None
    assert res == 'mocked_value'
