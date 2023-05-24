"""Document loader for loading documents from a directory."""
import os
import glob
from pathlib import Path
from typing import List
from dotenv import load_dotenv

from langchain.document_loaders import (
    CSVLoader,
    EverNoteLoader,
    PDFMinerLoader,
    TextLoader,
    UnstructuredEmailLoader,
    UnstructuredEPubLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    #UnstructuredODTLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
)

from langchain.docstore.document import Document


# Map file extensions to document loaders and their arguments
LOADER_MAPPING = {
    ".csv": (CSVLoader, {"csv_args": {"delimiter": ","}}),
    # ".docx": (Docx2txtLoader, {}),
    ".doc": (UnstructuredWordDocumentLoader, {}),
    ".docx": (UnstructuredWordDocumentLoader, {}),
    ".enex": (EverNoteLoader, {}),
    ".eml": (UnstructuredEmailLoader, {}),
    ".epub": (UnstructuredEPubLoader, {}),
    ".html": (UnstructuredHTMLLoader, {}),
    ".md": (UnstructuredMarkdownLoader, {}),
    #".odt": (UnstructuredODTLoader, {}),
    ".pdf": (PDFMinerLoader, {}),
    ".ppt": (UnstructuredPowerPointLoader, {}),
    ".pptx": (UnstructuredPowerPointLoader, {}),
    ".txt": (TextLoader, {"encoding": "utf8"}),
    # Add more mappings for other file extensions and loaders as needed
}

class DocumentLoader:
    """Document loader for loading documents from a directory."""

    @staticmethod
    def load_single_document(file_path: str or Path, **document_loader_kwargs) -> Document:
        """Load a single document from a file path."""
        if isinstance(file_path, str):
            file_path = Path(file_path)
        ext = file_path.suffix.lower()
        file_path = str(file_path)
        if ext in LOADER_MAPPING:
            loader_class, loader_args = LOADER_MAPPING[ext]
            loader_args.update(document_loader_kwargs)
            loader = loader_class(file_path, **loader_args)
            return loader.load()[0]

        raise ValueError(f"Unsupported file extension '{ext}'")

    @staticmethod
    def load_documents(source_dir: str or Path, **document_loader_kwargs) -> List[Document]:
        """Load all documents from source documents directory."""
        if isinstance(source_dir, str):
            source_dir = Path(source_dir)
        all_files = []
        for ext in LOADER_MAPPING:
            all_files.extend(source_dir.glob(f"*{ext}"))
        return [DocumentLoader.load_single_document(file_path, **document_loader_kwargs) for file_path in all_files]
