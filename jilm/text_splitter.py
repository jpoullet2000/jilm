from typing import List
from load_dotenv import load_dotenv
from langchain.docstore.document import Document
from langchain.text_splitter import TextSplitter, RecursiveCharacterTextSplitter

load_dotenv()

class TextSplitter:
    def __init__(self, text: str, max_tokens: int = 1000, chunk_size: int = 64, chunk_overlap: int = 0):
        self.text = text
        self.max_tokens = max_tokens
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, documents: List[Document]) -> List[Document]:
        """Split the text into chunks of max_tokens."""
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        texts = text_splitter.split_documents(documents)
        print(f"Loaded {len(documents)} documents")
        print(f"Split into {len(texts)} chunks of text (max. {self.chunk_size} characters each)")
        return texts
