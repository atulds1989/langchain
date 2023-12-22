from langchain.llms import openai
import os
from langchain import HuggingFaceHub
import warnings
warnings.filterwarnings('ignore')

from dotenv import load_dotenv

hf_key = os.getenv("hf_key")

llm_huggingface=HuggingFaceHub(huggingfacehub_api_token='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' ,repo_id="google/flan-t5-large",model_kwargs={"temperature":0,"max_length":64})


output=llm_huggingface.predict("Can you tell me the capital of China")
print(output)