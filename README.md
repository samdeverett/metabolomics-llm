# RAG for Metabolomics LLM

Code for pulling research papers from CORE and preprocessing them for retrieval-augmented generation to power a metabolomics LLM.

Requires putting a CORE API key (which you can get [here](https://core.ac.uk/services/api#form)) in a file called `apikey.py`.

Data for the query `"metabolomics AND language:English AND yearPublished:{year}"` can be found [here](https://drive.google.com/drive/folders/1DCWCLsF7ImHamxzl6tAz7nTZNO_dsvWt?usp=sharing) for years 2013 - 2023. If you'd like to use it, download the parquet files and place them in a `data` folder in the root directory.

### Potential Next Steps / TODOs

* Investigate distribution of number of chemical names in works.
    * Could subtract Oxford dictionary words from text and see what remains
    * Could do a search based on hmdb
* To increase number of papers, could include `"(nmr OR ms)"` or `"untargeted"` in the query alongside metabolomics
* Develop set of evalutation questions
    * A basic example might be "what happens to molecule x when human subjects are exposed to a bout of exercise?"
