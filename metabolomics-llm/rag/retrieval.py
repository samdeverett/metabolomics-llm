"""
This script provides functionality for creating a LangChain chain for retrieval QA. 
"""

from langchain.chains import RetrievalQA
from langchain.schema.language_model import BaseLanguageModel
from langchain.vectorstores.pinecone import Pinecone


def init_RetrievalQA(
        llm: BaseLanguageModel,
        chain_type: str = 'stuff',
        vectorstore: Pinecone,
        return_source_documents: bool = True
    ) -> RetrievalQA:
    """Initializes a RetrievalQA to answer questions over an index.
    
    Args:
        llm: The language model to use.
        chain_type: The chain type to use.
        vectorstore: The instance of a LangChain Pinecone vectorstore to use as the retriever.
        return_source_documents: Whether or not to return "source_documents" as part of the result.
    """
    retrieval_qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type=chain_type,
        retriever=vectorstore.as_retriever(),
        return_source_documents=return_source_documents
    )
    return retrieval_qa
