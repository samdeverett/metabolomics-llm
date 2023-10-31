"""
Vector indexes are used to store embeddings.
This script provides functionality for initializing and inserting documents to a vector index.
"""

import pandas as pd
import pinecone
import time

from langchain.embeddings.huggingface import HuggingFaceEmbeddings


def connect(api_key: str, environment: str) -> None:
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


def insert(
        index: pinecone.index.Index,
        data: pd.DataFrame,
        embed_model: HuggingFaceEmbeddings,
        batch_size: int = 100
    ) -> None:
    for i in range(0, len(data), batch_size):
        i_end = min(len(data), i + batch_size)
        batch = data.iloc[i:i_end]
        # make id's
        ids = [f"{row['id']}-{row['chunk_id']}" for _, row in batch.iterrows()]
        # generate embeddings
        texts = [row['chunk'] for _, row in batch.iterrows()]
        embeds = embed_model.embed_documents(texts)
        # add metadata
        metadata = [
            {'text': row['chunk'],
            'source': row['source'],
            'title': row['title']} for _, row in batch.iterrows()
        ]
        # store in Pinecone index
        index.upsert(vectors=zip(ids, embeds, metadata))
