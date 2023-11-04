"""
RAG requires being able to search for documents to feed as context to a prompt.
In order to search over documents, they must be embedded (i.e., translated from natural language into lists of numbers).
This script provides functionality for initializing an embedding model.
"""

from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from torch import cuda


def init_embed_model(model_name: str) -> HuggingFaceEmbeddings:
    device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'
    embed_model = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device': device},
        encode_kwargs={'device': device}
    )
    return embed_model
