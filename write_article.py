import autogen

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

assistant = autogen.AssistantAgent(
    name="Blogger",
    llm_config=llm_config,
    system_message="You are a software engineer and a populat tech blogger"
)

user_proxy = autogen.UserProxyAgent(
    name="smax",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=15,
    is_termination_msg=lambda x: x.get ("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir":"_output2", "use_docker":"python:3"},
    llm_config=llm_config,
    system_message=""""
    You are a professional article reviwer and software engineer. Carefully evaluate the taks and you peer answers. 
    Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved.
    """
)

task = """
Your task is to write an article about AutoGen. The idea is to give a quick start guide.
First, you need yo evaluate the docs about AutoGen at https://microsoft.github.io/autogen/, make sure to follow links at the web site and gather deep enough understanding of the library.
Second, you will be describing a sample project located at: https://github.com/maxim-saplin/autogen_sample/blob/main/write_article.py
Your result must be a markdown file named 'article.md' that will be used to publish it at a public blogging platform.

Article acceptance criteria:
- Engaging writing
- Reviews the concepts of AutoGen
- Reviews the sample project
- Provides code snippets
- Is a good starting point for a developer looking at starting to use AutoGen
- Is well structured
"""

user_proxy.initiate_chat(assistant, message=task)