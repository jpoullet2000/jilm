from jilm.doc_query import DocQuery
from jilm.text_splitter import TextSplitter
from jilm.document_loader import DocumentLoader

def test_doc_query(data_folder):
    splitter = TextSplitter()
    doc = DocumentLoader.load_single_document(data_folder / "paul_graham_essays_worked.txt")
    docs = splitter.split([doc])
    res = DocQuery("What does the author describe as good work?", docs=docs)
    answer, docs = res.run()
    assert res is not None
    assert answer is not None
    assert len(docs) > 1

