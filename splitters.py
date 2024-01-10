""" This module's purpose is splitting characters and no other functionality. """

# Import libraries
from langchain.text_splitter import RecursiveCharacterTextSplitter


class Splitter:
    def __init__(self, documents):
        """
        Initializes a new instance of the class.
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=100,
            length_function=len,
        )
        self.documents = documents

    def split_text(self):
        """
        Splits a list of documents into individual text documents.

        Returns:
            list: A list of split text from the input documents.
        """
        # Create documents from the input text
        text_documents = self.text_splitter.create_documents(self.documents)

        # Extract the split text from the documents
        split_text = [doc.page_content for doc in text_documents]

        return split_text


# Instantiation example when importing to other modules:
# splitter = Splitter(file_type_cache)
