from typing import List
from pygptj.model import Model
from langchain.vectorstores import Chroma
from chromadb.config import Settings
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA
from jilm.settings import llm_model, CHROMA_SETTINGS, embeddings, PERSIST_DIRECTORY


class DocQuery:
    def __init__(self, query: str, docs: List[Document], llm: Model = llm_model, chroma_settings: Settings = CHROMA_SETTINGS, embeddings=embeddings):
        self.query = query
        self.llm = llm
        self.chroma_settings = chroma_settings
        self.docs = docs
        self.embeddings = embeddings
        self._db = None

    def _db_from_doc(self):
        """Generate a chroma db from a list of document."""
        self._db = Chroma.from_documents(self.docs, self.embeddings, persist_directory=PERSIST_DIRECTORY, client_settings=CHROMA_SETTINGS)
        self._db.persist()

    def run(self):
        """Run the query on the documents."""
        retriever = self._db.as_retriever()
        qa = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
        res = qa(self.query)
        answer, docs = res['result'], res['source_documents']
        return answer, docs
