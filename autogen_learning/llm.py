# flake8: noqa: 266
import os
from dotenv import load_dotenv

load_dotenv()


def get_llm_config():
    llm_config = {
        "api_type": "azure",
        "model": os.environ["AZURE_OPENAI_DEPLOYMENT"],
        "api_key": os.environ["AZURE_OPENAI_KEY"],
        "base_url": os.environ["AZURE_OPENAI_ENDPOINT"],
        "api_version": os.environ["AZURE_OPENAI_VERSION"],
    }
    return llm_config
