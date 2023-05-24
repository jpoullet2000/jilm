from typing import List
from pathlib import Path
from pygptj.model import Model
from langchain.vectorstores import Chroma
from chromadb.config import Settings
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA
from jilm.settings import CHROMA_SETTINGS, embeddings, PERSIST_DIRECTORY
from jilm.document_loader import DocumentLoader
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from jilm.model import JILMLangModel

class DocQuery:
    def __init__(self, query: str, docs: List[Document] = None, doc_folder = Path or str, llm: Model = None, chroma_settings: Settings = CHROMA_SETTINGS, embeddings=embeddings):
        self.query = query
        self.llm = llm or JILMLangModel(callbacks=[StreamingStdOutCallbackHandler()])
        self.chroma_settings = chroma_settings
        self.docs = self._get_docs(docs, doc_folder)
        self.embeddings = embeddings
        self._db = None

    def _get_docs(self, docs: List[Document], doc_folder: Path or str) -> List[Document]:
        """Get a list of documents from a list of documents or a folder."""
        if docs is not None:
            return docs
        if doc_folder is not None:
            return self._get_docs_from_folder(doc_folder)
        raise ValueError("Either docs or doc_folder must be provided.")

    def _get_docs_from_folder(self, doc_folder: Path or str) -> List[Document]:
        """Get a list of documents from a folder."""
        if isinstance(doc_folder, str):
            doc_folder = Path(doc_folder)
        docs = []
        for file_path in doc_folder.glob("*"):
            docs.append(DocumentLoader.load_single_document(file_path))
        return docs

    def _db_from_doc(self):
        """Generate a chroma db from a list of document."""
        self._db = Chroma.from_documents(self.docs, self.embeddings, persist_directory=PERSIST_DIRECTORY, client_settings=CHROMA_SETTINGS)
        self._db.persist()

    def run(self):
        """Run the query on the documents."""
        if not self._db:
            self._db_from_doc()
        retriever = self._db.as_retriever()
        qa = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
        res = qa(self.query)
        answer, docs = res['result'], res['source_documents']
        return answer, docs
