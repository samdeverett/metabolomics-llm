# RAG for Metabolomics LLM

Code for pulling research papers from CORE and preprocessing them for retrieval-augmented generation to power a metabolomics LLM.

Requires putting a CORE API key (which you can get [here](https://core.ac.uk/services/api#form)) in `apikey.py`.

Data for the query `"metabolomics AND language:English AND yearPublished:{year}"` can be found [here](https://drive.google.com/drive/folders/1DCWCLsF7ImHamxzl6tAz7nTZNO_dsvWt?usp=sharing) for years 2013 - 2023. If you'd like to use it, download the parquet files and place them in a `data` folder in the root directory.
