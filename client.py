import os
from dotenv import load_dotenv
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

load_dotenv()


def get_azure_client():
    return AzureOpenAIChatCompletionClient(
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        model="gpt-4o",
        api_version=os.getenv("AZURE_OPENAI_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_KEY"),
    )
