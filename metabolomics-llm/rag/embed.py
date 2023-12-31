"""
RAG requires being able to search for documents to feed as context to a prompt.
In order to search over documents, they must be embedded (i.e., translated from natural language into lists of numbers).
This script provides functionality for initializing an embedding model.
"""

from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from torch import cuda


def init_embed_model(model_name: str) -> HuggingFaceEmbeddings:
    """Initializes an embedding model from Hugging Face.
    
    Args:
        model_name: The name of the Hugging Face embedding model.
    """
    device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'
    embed_model = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device': device},
        encode_kwargs={'device': device}
    )
    return embed_model


def get_embed_length(embed_model: HuggingFaceEmbeddings) -> int:
    """Returns the length of embeddings generated by a model.
    
    Args:
        embed_model: An initialized Hugging Face embedding model (see init_embed_model).
    """
    dummy_text = ["dummy"]
    dummy_embedding = embed_model.embed_documents(dummy_text)
    embed_length = len(dummy_embedding[0])
    return embed_length
