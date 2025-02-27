# https://github.com/microsoft/autogen/blob/47df9d53be9ba28da460c7344e3c8a37bdbbc24b/notebook/agentchat_RetrieveChat.ipynb#L22
# Run Docket desktop, add /Library/Frameworks/Python.framework/ tunder File Sharing options

import autogen

config_list = autogen.config_list_from_json(
    "config_list.json",
    file_location=".",
    filter_dict={
        "model": {
            "gpt35x16k",
            "gpt4x8k",
            }
        }
)

assert len(config_list) > 0
print("models to use: ", [config_list[i]["model"] for i in range(len(config_list))])

from autogen.retrieve_utils import TEXT_FORMATS

print("Accepted file formats for `docs_path`:")
print(TEXT_FORMATS)

from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
import chromadb

autogen.ChatCompletion.start_logging(compact=True)

# 1. create an RetrieveAssistantAgent instance named "assistant"
assistant = RetrieveAssistantAgent(
    name="assistant", 
    system_message="You are a helpful assistant.",
    llm_config={
        "request_timeout": 600,
        "seed": 42,
        "config_list": config_list,
    },
)

# 2. create the RetrieveUserProxyAgent instance named "ragproxyagent"
# By default, the human_input_mode is "ALWAYS", which means the agent will ask for human input at every step. We set it to "NEVER" here.
# `docs_path` is the path to the docs directory. By default, it is set to "./docs". Here we generated the documentations from FLAML's docstrings.
# Navigate to the website folder and run `pydoc-markdown` and it will generate folder `reference` under `website/docs`.
# `task` indicates the kind of task we're working on. In this example, it's a `code` task.
# `chunk_token_size` is the chunk token size for the retrieve chat. By default, it is set to `max_tokens * 0.6`, here we set it to 2000.
ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxyagent",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config={"use_docker":"python:3"},
    retrieve_config={
        "task": "code",
        "docs_path": "./website/docs/reference",
        "chunk_token_size": 2000,
        "model": config_list[0]["model"],
        "client": chromadb.PersistentClient(path="./chromadb"),
        "embedding_model": "all-mpnet-base-v2",
    },
)

print(autogen.ChatCompletion.logged_history)

#Ex 1

# reset the assistant. Always reset the assistant before starting a new conversation.
assistant.reset()

# given a problem, we use the ragproxyagent to generate a prompt to be sent to the assistant as the initial message.
# the assistant receives the message and generates a response. The response will be sent back to the ragproxyagent for processing.
# The conversation continues until the termination condition is met, in RetrieveChat, the termination condition when no human-in-loop is no code block detected.
# With human-in-loop, the conversation will continue until the user says "exit".

#code_problem = "How can I use FLAML to perform a classification task and use spark to do parallel training. Train 30 seconds and force cancel jobs if time limit is reached."
#ragproxyagent.initiate_chat(assistant, problem=code_problem, search_string="spark")  # search_string is used as an extra filter for the embeddings search, in this case, we only want to search documents that contain "spark".

print(autogen.ChatCompletion.logged_history)

#Ex 2

assistant.reset()

qa_problem = "Who is the author of FLAML?"
ragproxyagent.initiate_chat(assistant, problem=qa_problem)

print(autogen.ChatCompletion.logged_history)