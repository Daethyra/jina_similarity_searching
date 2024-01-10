import os
import logging
from typing import List
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.text_splitter import RecursiveCharacterTextSplitter


def load_split_dir(
    directory: str = "data", use_multithreading: bool = True
) -> List[str]:
    # Create a DirectoryLoader instance with multithreading enabled to load documents
    # recursively from the 'data' directory.
    loader = DirectoryLoader("data", use_multithreading=True, recursive=True)
    # Load the documents using the configured loader
    docs = loader.load_and_split(
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=0)
    )
