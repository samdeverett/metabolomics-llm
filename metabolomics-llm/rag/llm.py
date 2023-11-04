"""
This script provides functionality for initializing a LLM pipeline to be used in RAG.
"""

import transformers

from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from torch import cuda, bfloat16
from transformers.models.llama.modeling_llama import LlamaForCausalLM
from transformers.models.llama.tokenization_llama_fast import LlamaTokenizerFast
from transformers.pipelines.text_generation import TextGenerationPipeline
from typing import Dict, Any


def init_llm(model_id: str, hf_auth_token: str) -> LlamaForCausalLM:
    """Initializes a pretrained Hugging Face model.

    Args:
        model_id: The model id of a pretrained model configuration hosted inside a model repo on huggingface.co.
            Valid model ids can be located at the root-level, like bert-base-uncased,
            or namespaced under a user or organization name, like dbmdz/bert-base-german-cased.
        hf_auth_token: Hugging Face access token (https://huggingface.co/settings/tokens).
    """
    device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'
    
    # set quantization configuration to load large model with less GPU memory
    bnb_config = transformers.BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type='nf4',
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=bfloat16
    )

    # initialize Hugging Face model
    model_config = transformers.AutoConfig.from_pretrained(
        model_id,
        use_auth_token=hf_auth_token
    )

    # pull model in evaluation (not training) mode
    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_id,
        trust_remote_code=True,
        config=model_config,
        quantization_config=bnb_config,
        device_map='auto',
        use_auth_token=hf_auth_token
    )
    model.eval()

    return model


def init_tokenizer(model_id: str, hf_auth_token: str) -> LlamaTokenizerFast:
    """Initializes a pretrained Hugging Face model.

    Args:
        model_id: The model id of a pretrained tokenizer hosted inside a model repo on huggingface.co.
            Valid model ids can be located at the root-level, like bert-base-uncased,
            or namespaced under a user or organization name, like dbmdz/bert-base-german-cased.
        hf_auth_token: Hugging Face access token (https://huggingface.co/settings/tokens).
    """
    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_id,
        use_auth_token=hf_auth_token
    )
    return tokenizer


def init_text_generation_pipeline(
        model: LlamaForCausalLM,
        tokenizer: LlamaTokenizerFast,
        model_kwargs: Dict[str, Any] = {}
    ) -> TextGenerationPipeline:
    pass

def init_langchain_pipeline(pipeline: TextGenerationPipeline) -> HuggingFacePipeline:
    pipeline = HuggingFacePipeline(pipeline=pipeline)
    return pipeline
git 