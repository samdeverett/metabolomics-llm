"""
Vector indexes are used to store embeddings.
This script provides functionality for initializing and inserting documents to a vector index.
"""

import pandas as pd
import pinecone
import time


def connect(api_key: str, environment: str):
    """Connects to Pinecone environment."""
    pinecone.init(
        api_key=api_key,
        environment=environment
    )
    

def init_index(
        name: str,
        dimension: int,
        metric: str = 'cosine'
    ) -> pinecone.index.Index:
    """Creates and returns a Pinecone Index.
    
    Args:
        name: The name of the index to be created.
        dimension: The dimensions of the vectors to be inserted in the index.
        metric: The distance metric to be used for similarity search.
            The options are 'euclidean', 'cosine', or 'dotproduct'.
    """
    if name not in pinecone.list_indexes():
        pinecone.create_index(
            name=name,
            dimension=dimension,
            metric=metric
        )
    # wait for index to finish initialization
    while not pinecone.describe_index(name).status['ready']:
        time.sleep(1)
    index = pinecone.Index(name)
    return index
