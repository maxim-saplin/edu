# flake8: noqa: 266
import autogen
from llm import get_llm_config

llm_config = get_llm_config()

entry_point = autogen.ConversableAgent(
    name="Entry_Point",
    llm_config=llm_config,
)

agent1 = autogen.ConversableAgent(
    name="Agent_1",
    llm_config={
        **llm_config,
        "temperature": 1.0
    },
)

agent2 = autogen.ConversableAgent(
    name="Agent_2",
    llm_config={
        **llm_config,
        "temperature": 0.0
    },
)

def reflection_message(recipient, messages, sender, config):
    return f"""{recipient.chat_messages_for_summary(sender)[-1]['content']}"""

nested_chats = [
    {
        "recipient": agent1,
        "max_turns": 1,
        "message": reflection_message,
    },
    {
        "recipient": agent2,
        "max_turns": 1,
        "message": reflection_message,
    },
]

entry_point.register_nested_chats(
    nested_chats,
    trigger=entry_point,
)

chat_result = entry_point.initiate_chat(
    recipient=entry_point, message="Write JavaScript function under 5 lines calculating factorial of a number", 
    max_turns=1, 
    summary_method="reflection_with_llm",
    summary_prompt="""\
You have been provided with a set of responses from various open-source models to the latest user query.
Your task is to synthesize these responses into a single, high-quality response in British English spelling.
It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect.
Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction.
Ensure your response is well-structured, coherent and adheres to the highest standards of accuracy and reliability.
""",
)