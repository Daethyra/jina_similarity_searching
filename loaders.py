import os
import logging
from langchain_community.document_loaders import UnstructuredFileLoader

# Load list of files in subdir 'data'


# Iteratively use UnstructuredFileLoader against list of files
    # Release each file forward for further processing upon completion
        # Use `RecursiveCharacterTextSplitter` iteratively against released files