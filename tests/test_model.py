from jilm.model import JILMLangModel


def test_jilmlangmodel():
    res = JILMLangModel().generate(["Hello, world!"])
    assert res is not None
