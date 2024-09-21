# flake8: noqa: 266
import os
import pprint
from dotenv import load_dotenv
from autogen import ConversableAgent


load_dotenv()

llm_config = {
    "api_type": "azure",
    "model": os.environ["AZURE_OPENAI_DEPLOYMENT"],
    "api_key": os.environ["AZURE_OPENAI_KEY"],
    "base_url": os.environ["AZURE_OPENAI_ENDPOINT"],
    "api_version": os.environ["AZURE_OPENAI_VERSION"],
}

## Using agents as simple LLM interface

agent = ConversableAgent(
    name="chatbot",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

# generate_reply() doesn't alter state (do not alter dialog)
reply = agent.generate_reply(messages=[{"content": "Tell me a joke.", "role": "user"}])
print(reply)

# Hence in here the reply will be asking which joke to repeate, the above reply is missing from the chat dialog,
# the whole dialog is passed in as a whole in messages
reply = agent.generate_reply(messages=[{"content": "Repeat the joke.", "role": "user"}])
print(reply)
print("\n\n\n\n")

## Conversation between standup commedians

cathy = ConversableAgent(
    name="cathy",
    system_message="Your name is Cathy and you are a stand-up comedian.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

joe = ConversableAgent(
    name="joe",
    system_message="Your name is Joe and you are a stand-up comedian. "
    "Start the next joke from the punchline of the previous joke.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

# Finishing after 2nd turn - i.e. after 2nd assistnt reply (cathy) OR after the 4th message in the chat
chat_result = joe.initiate_chat(
    recipient=cathy,
    message="I'm Joe. Cathy, let's keep the jokes rolling.",
    max_turns=2,
)

## Inspecting chat result

# $ and tokens
pprint.pprint(chat_result.cost)
# By default prints the last message but can be cuustomized
pprint.pprint(chat_result.summary)
# Whole conversation in JSON as one would expect in OpenAI Chat Completions API
pprint.pprint(chat_result.chat_history)
print("\n\n\n\n")

## Configuring chat to use the same LLM to summarize the conversattion

chat_result = joe.initiate_chat(
    cathy,
    message="I'm Joe. Cathy, let's keep the jokes rolling.",
    max_turns=2,
    summary_method="reflection_with_llm",
    summary_prompt="Summarize the conversation",
)

pprint.pprint(chat_result.summary)
print("\n\n\n\n")

## Stop Phrase - determining termination condition

cathy = ConversableAgent(
    name="cathy",
    system_message="Your name is Cathy and you are a stand-up comedian. "
    "Don't make the conversation long and boring, say 'I gotta go' (return exactly 'I gotta go') to end the conversation.",
    # "When you're ready to end the conversation, say 'I gotta go'.",
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "I gotta go" in msg["content"],
)

joe = ConversableAgent(
    name="joe",
    system_message="Your name is Joe and you are a stand-up comedian. "
    "Don't make the conversation long and boring, say 'I gotta go' (return exactly 'I gotta go') to end the conversation.",
    # "When you're ready to end the conversation, say 'I gotta go'.",
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "I gotta go" in msg["content"]
    or "Goodbye" in msg["content"],
)

chat_result = joe.initiate_chat(
    recipient=cathy, message="I'm Joe. Cathy, let's keep the jokes rolling."
)

print("\n\n\n\n")
# Continueing the conversation
cathy.send(message="What's last joke we talked about?", recipient=joe)

## Notes
# The last part is very prominent showing how hard it can be to steer the conversation and set up stop condition.
# With default prompt and GPT-4o Mini are got very long never ending conversations, had to update the prompts.
# Sometime there were akward dialogs (multiple goodbyes) or smth like that (contunuing conversation didn't give the last joke)
# cathy (to joe):
# What's last joke we talked about?
# --------------------------------------------------------------------------------
# joe (to cathy):
# I gotta go.
