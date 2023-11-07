"""
This script puts together all the functionality needed to run RAG end-to-end.
"""

import embed
import index
import pipeline
import retrieve

from apikey import PINECONE_API_KEY, PINECONE_ENV, HF_AUTH_TOKEN



