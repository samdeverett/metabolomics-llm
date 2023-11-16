# RAG for Metabolomics LLM

This repo contains code for using retrieval-augmented generation (RAG) to power a metabolomics LLM.

The goal of the project is to create a virtual research assistant specialized in [metabolomics](https://en.wikipedia.org/wiki/Metabolomics) capable of answering questions in detail, generating hypotheses, and synthesizing results. It uses Llama 2 within a Hugging Face text generation transformer.

For a demo, check out [`metabolomics-llm/demo/demo.ipynb`](https://github.com/samdeverett/metabolomics-llm/blob/main/metabolomics-llm/demo/demo.ipynb).

## UPDATE (11/16/23)

Due to the recent launch of CustomGPTs and Assistants with Retrieval from OpenAI, we have decided to put this project on hold. It is clear that the development of AI research assistants is accelerating at rates we cannot keep up with as independent, part-time developers. We have pivoted focus to exploring existing solutions for our use case, including the development of our own CustomGPT, the use of others CustomGPTs, and open-source frameworks for advanced RAG like [LlamaIndex](https://www.llamaindex.ai). That said, the code in this repository still works, and it can be a useful exercise to understand it in order to understand what is going on – at a high level – under the hood of more complex systems. If you're interested in this, we suggest checking out the [demo](https://github.com/samdeverett/metabolomics-llm/blob/main/metabolomics-llm/demo/demo.ipynb) and it's underlying [functions](https://github.com/samdeverett/metabolomics-llm/tree/main/metabolomics-llm/rag).

## Installation

1.  Clone the Repository:

    ```shell
    git clone -b main hhttps://github.com/samdeverett/metabolomics-llm.git
    cd metabolomics-llm
    ```

2.  (Optional) Activate a Virtual Environment, e.g.:

    ```shell
    conda create -n metabolomics-llm python=3.9
    conda activate metabolomics-llm
    ```

3.  Install Requirements:

    ```shell
    pip install -r requirements.txt
    ```

### API Keys

To pull research papers from [CORE](https://core.ac.uk), you'll need an API key from [here](https://core.ac.uk/services/api#form).

To connect to a [Pinecone](https://www.pinecone.io) vector database, you'll have to register and get an API key along with an environment name.

To access models from Hugging Face, you'll have to register and create a token [here](https://huggingface.co/settings/tokens).

Various scripts and notebooks require these credentials.

## Organization

- `demo` contains a demo of how RAG is implemented to provide high-quality responses to metabolomics related questions.

- `rag` contains scripts with the functions necessary for performing RAG as in the demo

- `glutamate` is a deeper proof-of-concept into a language model's ability to synthesize results from various papers.
    > Note that this is unfinished as per the update above.

- `data.py` contains code for querying research papers from the CORE API.
    > Data for the query `"metabolomics AND language:English AND yearPublished:{year}"` can be found [here](https://drive.google.com/drive/folders/1DCWCLsF7ImHamxzl6tAz7nTZNO_dsvWt?usp=sharing) for years 2000 - 2023. If you'd like to use it, download the parquet files and place them in a `data` folder in the `metabolomics-llm` folder.

- `eda.ipynb` contains basic exploratory data analysis of the research papers pulled.

- `utils.py` provides helper functions.

## Safety Statement

We take seriously the risk of developing dangerous AI capabilities. We imagine that these may emerge in one of two ways: 1) creating an AI system that is independently capable of producing catastrophic outcomes (e.g., biohacking, mass poisoning, etc.), or 2) making it easier for malicious human actors to bring about catastrophic outcomes.

We do not believe that this project advances either of these risks. Our reasons for believing this stem from four main considerations.

1. **Training Data.** The system we develop here is trained exclusively on text describing experiments, not on any empirical data from the experiments themselves. In other words, we are creating a system that interprets and regurgitates humans' interpretations of experimental data. We believe that the distinction between training on textual interpretations versus raw data is critical: it ensures that humans remain in charge of examining results, and it prohibits the AI system from running analyses of its own.

2. **System Design**. The system we develop here exclusively uses retrieval-augmented generation (RAG), not fine-tuning. None of the LLM's weights are being changed; only the prompts passed to the LLM are being updated. Put differently, we are not actually training any models. Consequently, it does not seem possible that the LLM would learn dangerous behaviors (e.g., deception, sycophancy, power-seeking, etc.). However, if such behaviors already exists in the base model--which, to the best of our knowledge, is not the case--then we would also expect to have them in this system. One threat we are particularly mindful of is the LLM's potential ability to autonomously query the vector database we created, allowing it to access that information without us knowing. We have not seen any evidence of this happening (in any RAG system) but will be quick to shut this down if that changes.

3. **System Agency**. The system we develop here is exclusively for question-answering. All of its outputs go back to humans in the form of text. It is not connected to other systems and does not have agency beyond producing text. As mentioned above, if there is evidence of this changing, we will be quick to shut it down (e.g., delete the vector database).

4. **Science Regulation**. The goal of the system we develop here is to catalyze metabolomics research by giving researchers access to better search techniques, syntheses of results, hypotheses, and potential experiments. To the extent that we trust researchers and regulatory bodies in this field, we can trust that the system will be used for positive progress. If there does exist a malicious researcher who seeks to use this system for developing harmful ideas, they will still be subject to the same forces of oversight that disincentivize this behavior. We do not expect this system to further enable a malicious actor who is not familiar with metabolomics because the outputs of the RAG system are just as jargony as the original open-source papers and the resources required to do metabolomics experiments even after having an idea are not accessible to people outside specific labs.

 **All these reasons aside, out of an abundance of caution, we are not yet publicly launching this application nor sharing the vector database of embeddings.** We do note, however, that money is really the only barrier to replicating our results given that the base LLM, corpus of training data, and tools for implementing RAG are all freely available and open-source.

 If you believe we are improperly assessing the risks of this project and/or have suggestions on how we may better evaluate its risk, please [let us know](mailto:samdev@mit.edu).

 If you are a researcher interested in gaining access to the application, please [send us a message](mailto:samdev@mit.edu).
