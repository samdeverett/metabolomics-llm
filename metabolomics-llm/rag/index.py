"""
Vector indexes are used to store embeddings.
This script provides functionality for initializing and inserting documents to a vector index.
"""

import pandas as pd
import pinecone
import time

from langchain.embeddings.huggingface import HuggingFaceEmbeddings


class Index():

    def __init__(self) -> None:
        pass


    def init_index(self) -> None:
        """Run logic to initialize the index."""
        pass


    def insert(self, data: pd.DataFrame) -> None:
        """Insert data into the index."""
        pass


class Pinecone(Index):

    def __init__(self,
            api_key: str,
            environment: str,
            name: str,
            dimension: int,
            metric: str = 'cosine'
        ) -> None:
        super().__init__()
        self.connect(api_key, environment)
        self.index = self.init_index(name, dimension, metric)


    def connect(self, api_key: str, environment: str) -> None:
        """Connects to Pinecone environment.
        
        Args:
            api_key: Pinecone API key.
            environment: Name of environment hosting the index.
        """
        pinecone.init(
            api_key=api_key,
            environment=environment
        )

    
    def init_index(self,
            name: str,
            dimension: int,
            metric: str
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


    def insert(self,
            data: pd.DataFrame,
            embed_model: HuggingFaceEmbeddings,
            batch_size: int = 100
        ) -> None:
        """Inserts data into the index.
        
        Args:
            data: A DataFrame containing the data to be inserted.
                The DataFrame must contain the following columns:
                    id: ID of the document.
                    chunk_id: ID of the chunk. This should be unique for every chunk per document.
                    text: Text of the chunk.
                    source: URL to the document.
                    title: Title of the document.
            embed_model: Embedding model used to generate embeddings of data.
            batch_size: Number of data points to insert at once.
        """
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
            self.index.upsert(vectors=zip(ids, embeds, metadata))
