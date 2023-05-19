from typing import List
from load_dotenv import load_dotenv

load_dotenv()

class TextSplitter:
    def __init__(self, text: str, max_tokens: int = 1000, chunk_size: int = 64, chunk_overlap: int = 0):
        self.text = text
        self.max_tokens = max_tokens
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self) -> List[str]:
        """Split the text into chunks of max_tokens."""
