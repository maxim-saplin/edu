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
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

assistant = autogen.AssistantAgent(
    name="CTO",
    llm_config=llm_config,
    system_message="Chief technical officer of a tech company"
)

user_proxy = autogen.UserProxyAgent(
    name="smax",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get ("content", "").rstrip() .endswith("Terminate"),
    code_execution_config={"work_dir":"_output", "use_docker":"python:3"},
    llm_config=llm_config,
    system_message=""""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
1. Write Python script that saves the contents of the article `https://dev.to/maximsaplin/efficient-dart-part-2-going-competitive-307c` to a .txt file
2. Then the script counts words and builds a histogram with word frequency, saves results to another .txt file with words sorted from most frequent to the least
3. Check the produced histogram and try guessing what the article is about, save thr results to `summary.txt`
4. Store the Python script in `process.py` file

Use Python. If there're any dependencies required please specifically tell me how to get them installed.
"""

user_proxy.initiate_chat(assistant, message=task)