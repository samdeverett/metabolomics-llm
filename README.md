# RAG for Metabolomics LLM

Code for enabling retrieval-augmented generation (RAG) to power a metabolomics LLM.

For a demo, check out `mvp/mvp.ipynb`.

---

### Requirements

#### API Keys
* Put your CORE API key (which you can get [here](https://core.ac.uk/services/api#form)) in a file called `apikey.py`.
* Put your [Pinecone](https://www.pinecone.io) API key and environment name in a file under the `mvp` folder called `apikey.py`.
* Put a Hugging Face token (which you can get [here](https://huggingface.co/settings/tokens)) in the `apikey.py` file under the `mvp` folder.

---

### Repo Structure

`mvp` contains a demo of how RAG is implemented to provide high-quality responses to metabolomics related questions.

`data.py` contains code for pulling works from the [CORE](https://core.ac.uk) API.
> Data for the query `"metabolomics AND language:English AND yearPublished:{year}"` can be found [here](https://drive.google.com/drive/folders/1DCWCLsF7ImHamxzl6tAz7nTZNO_dsvWt?usp=sharing) for years 2013 - 2023. If you'd like to use it, download the parquet files and place them in a `data` folder in the root directory.

`eda.ipynb` walks through exploratory data analysis of the data.

`preprocessing.ipynb` handles processing the data based on insights learned from EDA to prepare for RAG.

`utils.py` provides helper functions.

---

#### Potential Next Steps

* Investigate distribution of number of chemical names in works.
    * Could subtract Oxford dictionary words from text and see what remains
    * Could do a search based on hmdb
* To increase number of papers, could include `"(nmr OR ms)"` or `"untargeted"` in the query alongside metabolomics
* Develop set of evalutation questions
    * A basic example might be "what happens to molecule x when human subjects are exposed to a bout of exercise?"
