from jilm.doc_query import DocQuery

def test_doc_query(data_folder):
    res = DocQuery("Hello, world!", docs=None, doc_folder=data_folder)
    assert res is not None
