import autogen
# from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
import chromadb

config_list = autogen.config_list_from_json(
    "config_list.json",
    file_location=".",
    filter_dict={
        "model": {
            #"gpt35x16k",
            "gpt4x8k",
            }
        })

llm_config={
    "request_timeout": 700,
    "seed": 1,
    "config_list": config_list,
    "temperature": 0,
}

# web_surfer = RetrieveUserProxyAgent(
#     name="Web-Surfer",
#     is_termination_msg=lambda x: x.get ("content", "").rstrip().endswith("TERMINATE"),
#     system_message="Assistant who has extra content retrieval power for solving difficult problems",
#     human_input_mode="NEVER",
#     max_consecutive_auto_reply=3,
#     retrieve_config={
#         "task": "code",
#         "chunk_token_size": 1000,
#         "model": config_list[0]["model"],
#         "client": chromadb.PersistentClient(path="/tmp/chromadb"),
#         "collection_name": "groupchat",
#         "get_or_create": True,
#     },
#     code_execution_config=False,  # we don't want to execute code in this case.
# )

web_surfer = RetrieveAssistantAgent(
    name="assistant", 
    system_message="You are a helpful assistant.",
    code_execution_config=False,
    llm_config={
        "request_timeout": 600,
        "seed": 42,
        "config_list": config_list,
    },
)

blogger = autogen.AssistantAgent(
    name="Blogger",
    llm_config=llm_config,
    code_execution_config=False,
    system_message="You are a software engineer and a popular tech blogger"
)

reviewer = autogen.UserProxyAgent(
    name="Reviewer",
    llm_config=llm_config,
    human_input_mode="TERMINATE",
    is_termination_msg=lambda x: x.get ("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config=False,
    #code_execution_config={"work_dir":"_output2", "use_docker":"python:3"},
    system_message="You are a software engineer and a professional article reviewer"
)

# user_proxy = autogen.UserProxyAgent(
#     name="smax",
#     human_input_mode="TERMINATE",
#     max_consecutive_auto_reply=15,
#     is_termination_msg=lambda x: x.get ("content", "").rstrip().endswith("TERMINATE"),
#     #code_execution_config={"work_dir":"_output2", "use_docker":"python:3"},
#     llm_config=llm_config,
#     # system_message=""""
#     # You are a professional article reviwer and software engineer. Carefully evaluate the taks and you peer answers. 
#     # Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved.
#     # """
# )

task = """
Your task is to write an article about AutoGen. The idea is to give a quick start guide.
First,evaluate the docs about AutoGen at https://microsoft.github.io/autogen/. Make sure to follow links at the web site and gather deep enough understanding of the library. Please create a web crawl plan, present the pages and write down parts that might be relevant to our task.
Second, describe sample project located at: https://github.com/maxim-saplin/autogen_sample/blob/main/write_article.py
Your result must be a markdown file named 'article.md' that will be used to publish it at a public blogging platform.

Article acceptance criteria:
- Engaging writing
- Reviews the concepts of AutoGen
- Reviews the sample project
- Provides code snippets
- Is a good starting point for a developer looking at starting to use AutoGen
- Is well structured
"""

groupchat = autogen.GroupChat(
    agents=[web_surfer, blogger, reviewer], messages=[], max_round=12
)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

reviewer.initiate_chat(
    manager,
    message=task,
    n_results=3,
)
