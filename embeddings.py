"""Module for embedding documents using Jina AI's embedding capabilities."""

import logging
from typing import List
from langchain_community.embeddings.jina import JinaEmbeddings


def embed_documents(docs: List[str]) -> List[List[float]]:
    """
    Embeds a list of documents using JinaEmbeddings.

    Args:
        docs (List[str]): A list of documents to be embedded.

    Returns:
        List[List[float]]: A list of embedded documents, where each embedded document is represented as a list of floats.
    """
    # Create an instance of JinaEmbeddings
    jina_embeddings = JinaEmbeddings(
        jina_api_key=JINA_API_KEY,
        model_name="jina-embeddings-v2-small-en",
    )
    logging.info("Loaded JinaEmbeddings")

    # Embed the split documents using JinaEmbeddings
    logging.info("Beginning the embedding process...")
    embeddings = jina_embeddings.embed_documents(docs)
    logging.info("Finished embedding documents using JinaEmbeddings")

    return embeddings
