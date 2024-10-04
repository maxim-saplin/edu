# flake8: noqa: 266
import datetime
import pprint
from llm import get_llm_config
from autogen import ConversableAgent, AssistantAgent, GroupChat, GroupChatManager


llm_config = get_llm_config()

task = (
    "Write a blogpost about the stock price performance of "
    f"Nvidia in the past month. Today's date is {datetime.datetime.now().date()}"
)

## Group chat

# - User_proxy or Admin: to allow the user to comment on the report and ask the writer to refine it.
# - Planner: to determine relevant information needed to complete the task.
# - Engineer: to write code using the defined plan by the planner.
# - Executor: to execute the code written by the engineer.
# - Writer: to write the report.
# - Manager: broadcasts messages and picks the next speaker

user_proxy = ConversableAgent(
    name="Admin",
    system_message="Give the task, and send "
    "instructions to writer to refine the blog post.",
    code_execution_config=False,
    llm_config=llm_config,
    human_input_mode="ALWAYS",
)

planner = ConversableAgent(
    name="Planner",
    system_message="Given a task, please determine "
    "what information is needed to complete the task. "
    "Please note that the information will all be retrieved using"
    " Python code. Please only suggest information that can be "
    "retrieved using Python code. "
    "After each step is done by others, check the progress and "
    "instruct the remaining steps. If a step fails, try to "
    "workaround",
    # While system message is used to prime LLM with role, this one is used
    # to introduce the agent to other participants of the group chat
    description="Planner. Given a task, determine what "
    "information is needed to complete the task. "
    "After each step is done by others, check the progress and "
    "instruct the remaining steps",
    llm_config=llm_config,
)

engineer = AssistantAgent(
    name="Engineer",
    llm_config=llm_config,
    description="An engineer that writes code based on the plan "
    "provided by the planner.",
)

executor = ConversableAgent(
    name="Executor",
    system_message="Execute the code written by the " "engineer and report the result.",
    human_input_mode="NEVER",
    code_execution_config={
        "last_n_messages": 3,
        "work_dir": "coding_l6",
        "use_docker": "python:3.11-slim",
    },
)

writer = ConversableAgent(
    name="Writer",
    llm_config=llm_config,
    system_message="Writer."
    "Please write blogs in markdown format (with relevant titles)"
    " and put the content in pseudo ```md``` code block. "
    "You take feedback from the admin and refine your blog.",
    description="Writer."
    "Write blogs based on the code execution results and take "
    "feedback from the admin to refine the blog.",
)

groupchat = GroupChat(
    agents=[user_proxy, engineer, writer, executor, planner],
    messages=[],
    max_round=30,
    # Below 2 params are used to define speaker selection prolicy and are optional
    allowed_or_disallowed_speaker_transitions={
        # Sender : allowed recipients
        user_proxy: [engineer, writer, executor, planner],
        engineer: [user_proxy, executor],
        writer: [user_proxy, planner],
        executor: [user_proxy, engineer, planner],
        planner: [user_proxy, engineer, writer],
    },
    speaker_transitions_type="allowed",
)

manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# GPT-o4-mini failed to select the right next speaker (Planner) and
# selecting Writer as the 1st speaker who jumos to writing the report right away without any inputs
# GPT-o4 did the selection right and completed the flow yet it didn't suceed running the code and it
# didn't manage to provide and input data to the Writer, yet the writer did produce the report :)
# Luckily it used XXX placeholder for he actual numbers
# When I used speaker policy the agents did better managing to run code and get stock prices
# Emty user inouts had few gratitude loops with agents not able to complete the chain -> termination conditions are tricky
groupchat_result = user_proxy.initiate_chat(
    manager,
    message=task,
)

pprint.pprint(groupchat_result.cost)
pprint.pprint(groupchat_result.chat_history)
