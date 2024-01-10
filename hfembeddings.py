""" This module offers a localized way of embedding documents. This ensures privacy by running the open-source Jina AI embeddings model on your machine. """

from typing import List
from transformers import AutoTokenizer, AutoModel

class HfEmbeddingWrapper:
    """
    A wrapper class for handling Hugging Face embeddings.

    This class provides a convenient interface for loading a pretrained model and tokenizer,
    and encoding documents into embeddings.

    Attributes:
        tokenizer: An instance of the AutoTokenizer class from the transformers library.
        model: An instance of the AutoModel class from the transformers library.
    """
    def __init__(self):
        """
        Initializes the HfEmbeddingWrapper with a pretrained model and tokenizer.

        The model and tokenizer are downloaded from the "jinaai/jina-embeddings-v2-small-en" repository on Hugging Face.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(
            "jinaai/jina-embeddings-v2-small-en",
            trust_remote_code=True
        )
        self.model = AutoModel.from_pretrained("jinaai/jina-embeddings-v2-small-en")

    def embed_documents(self, docs: List[str]) -> List[List[float]]:
        """
       Encodes a list of documents into embeddings.

       Args:
           docs: A list of strings representing the documents to encode.

       Returns:
           A list of lists of floats representing the embeddings of the input documents.
       """
        model = self.model
        tokenizer = self.tokenizer
        embeddings = model.encode([docs])
    
    return embeddings
