# flake8: noqa: 266
import json
from autogen import ConversableAgent, initiate_chats
from llm import get_llm_config

llm_config = get_llm_config()

# Simulating 3-step "Customer Onboarding" flow: (1) Collect Customer info, (2) Get Interests, (3) Engange
# Each step implemented via 1-1 chat (LLM Agent with User via proxy agent)

## Agents

onboarding_personal_information_agent = ConversableAgent(
    # Had to add underscopre, don't know why yet with default values from the tutorial
    # I got error after the first user input
    # 400 {'message': "Invalid 'messages[1].name': string does not match pattern. Expected a string that matches the pattern '^[a-zA-Z0-9_-]+$'."
    # Seems like that is some message field in OpenAI API (same use role and message) which I didn't know about before: https://community.openai.com/t/discovered-how-a-name-is-added-to-api-chat-role-messages-and-the-tokens/330016
    name="Onboarding_Personal_Information_Agent",
    system_message="""You are a helpful customer onboarding agent,
    you are here to help new customers get started with our product.
    Your job is to gather customer's name and location.
    Do not ask for other information. Return 'TERMINATE' 
    when you have gathered all the information.""",
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
)

onboarding_topic_preference_agent = ConversableAgent(
    name="Onboarding_Topic_Preference_Agent",
    system_message="""You are a helpful customer onboarding agent,
    you are here to help new customers get started with our product.
    Your job is to gather customer's preferences on news topics.
    Do not ask for other information.
    Return 'TERMINATE' when you have gathered all the information.""",
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
    # adding this to skip 2nd turn if location/name are in one message doesn't help skipping the 2nd turn in the 1st chat
    is_termination_msg=lambda msg: "terminate" in msg.get("content").lower(),
)

customer_engagement_agent = ConversableAgent(
    name="Customer_Engagement_Agent",
    system_message="""You are a helpful customer service agent
    here to provide fun for the customer based on the user's
    personal information and topic preferences.
    This could include fun facts, jokes, or interesting stories.
    Make sure to make it engaging and fun!
    Return 'TERMINATE' when you are done.""",
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "terminate" in msg.get("content").lower(),
)

# That is not an agent, this is essential a way to get input from the users and channel it into chat
customer_proxy_agent = ConversableAgent(
    name="customer_proxy_agent",
    llm_config=False,
    code_execution_config=False,
    # Always get input from person
    human_input_mode="ALWAYS",
    is_termination_msg=lambda msg: "terminate" in msg.get("content").lower(),
)

## Creating tasks as 3 separate 2-agent chats

chats = [
    # Don't like it is non-typed dictionary with mannualy typed keys, so easy to make a mistake... Hate this non type-safe code
    {
        "sender": onboarding_personal_information_agent,
        "recipient": customer_proxy_agent,
        "message": "Hello, I'm here to help you get started with our product. "
        "Could you tell me your name and location?",
        # The next summary args and clear history are used to produce a single message output which will be relayed to the next chat
        # Sidenote, what I never liked about Autogen are those magic strings. How should I know it is "reflection_with_llm"...
        # Is it that hard to use Enums and get intellisense and tpye safety?
        "summary_method": "reflection_with_llm",
        "summary_args": {
            "summary_prompt": "Return the customer information "
            "into as JSON object only: "
            # asking to return JSON serves no purpose, structured output is not usde by program code YET it can mess the prompt chain and LLM thinking process downstream...
            # Though it is good to know that if you need a structured output you can use a feature of LLM summarizer
            # and get the structured output via "NL-to-Format (2 step, first Natural Language answer → convert to JSON)"
            "{'name': '', 'location': ''}",
        },
        # Not sure what this does in this sample, tried both and didn't see any differece.
        # Reading docs says it clears agent's history, seems irrelevant in our case as agents are not reused
        "clear_history": False,  # True,
        # What bugs me is that termination message is controlled in agent while number of turns in chat, yet it seems
        # that max turns and terminstion are two kinds of same thing - terminationc condition, not sure why different
        # kind of entities are used
        # "max_turns": 2,
    },
    {
        "sender": onboarding_topic_preference_agent,
        "recipient": customer_proxy_agent,
        "message": "Great! Could you tell me what topics you are "
        "interested in reading about?",
        # Will use built-in default summarization prompt
        "summary_method": "reflection_with_llm",
        "max_turns": 1,
        "clear_history": False,
    },
    {
        "sender": customer_proxy_agent,
        "recipient": customer_engagement_agent,
        "message": "Let's find something fun to read.",
        "max_turns": 1,
        "summary_method": "reflection_with_llm",
    },
]

## Onboarding Process - start the conversation with the user

chat_results = initiate_chats(chats)

# The first chat asks "Could you tell me your name and location?", and if I reply with "Minsk, Maxim"
# (not as demonstrated in the lessson where a user did 2 seperate messages with name and location, notice how I change the order of name/location),
# the LLM right away extracts all required data and returns TERMINATE, though the agent doesn't check for the condition and asks again the user.
# E.g.:
# Onboarding_Personal_Information_Agent (to customer_proxy_agent):
# Thank you, Maxim, from Minsk. You've provided all the information I need.
# TERMINATE
# --------------------------------------------------------------------------------
# Replying as customer_proxy_agent. Provide feedback to Onboarding_Personal_Information_Agent. Press enter to skip and use auto-reply, or type 'exit'

## Disecting chats

print("\n\n\n\Summaries: >>>>>>>>>>>>>>>\n\n")
for chat_result in chat_results:
    print(f"{chat_result.summary}\n--------------")

print("\n\n\n\Full chats: >>>>>>>>>>>>>>>\n\n")
for chat_result in chat_results:
    print(json.dumps(chat_result.chat_history, indent=4))
    print("--------------")

# It is so great that you can get full chat rols and see how the framework chains the prompts EXACTLY - something you can't easily do in Crew.ai
# Though there're no traces of summarizer, you just get the result of it in the next chat :)
# As you can see below the endings/summaries of previous chats are passed into following ones delimiting those with "\nContext:" which
# is very similar how it is done in Crewai tasks, exactly the same approach (even the same "\nContext" delimiter):
# [
#     {
#         "content": "Hello, I'm here to help you get started with our product. Could you tell me your name and location?",
#         "role": "assistant",
#         "name": "Onboarding_Personal_Information_Agent"
#     },
#     {
#         "content": "Minsk, Maxim",
#         "role": "user",
#         "name": "customer_proxy_agent"
#     },
#     {
#         "content": "Thank you, Maxim, from Minsk. You've provided all the information I need. \n\nTERMINATE",
#         "role": "assistant",
#         "name": "Onboarding_Personal_Information_Agent"
#     }
# ]
# --------------
# [
#     {
#         "content": "Great! Could you tell me what topics you are interested in reading about?\nContext: \n```json\n{'name': 'Maxim', 'location': 'Minsk'}\n```",
#         "role": "assistant",
#         "name": "Onboarding_Topic_Preference_Agent"
#     },
#     {
#         "content": "cars",
#         "role": "user",
#         "name": "customer_proxy_agent"
#     }
# ]
# --------------
# [
#     {
#         "content": "Let's find something fun to read.\nContext: \n```json\n{'name': 'Maxim', 'location': 'Minsk'}\n```\nMaxim is interested in reading about cars.",
#         "role": "assistant",
#         "name": "customer_proxy_agent"
#     },
#     {
#         "content": "Hey Maxim! \ud83d\ude97\u2728 Since you're into cars, how about we rev up your reading with some fun car facts and a little humor?\n\n### Fun Car Facts:\n1. **Fastest Car on Earth**: The Bugatti Chiron Super Sport 300+ holds the record, reaching speeds of 304 mph! That's faster than a cheetah! \ud83d\udc06\n2. **World's First Car**: The first gasoline-powered car was invented by Karl Benz in 1885. It had three wheels and a very cozy seating area\u2014perfect for a stylish ride around the block!\n3. **Self-Driving Cars**: Companies like Tesla and Waymo are working on autonomous vehicles that can drive themselves! Imagine not having to fight for the driver's seat on a road trip! \ud83d\ude99\n4. **Color Preference**: Studies show that 40% of car buyers prefer blue cars! What about you? Are you more of a red, black, or maybe a neon green kind of person? \ud83c\udfa8\n\n### Car Joke:\nWhy did the car bring a ladder to the bar?\nBecause it heard the drinks were on the house! \ud83c\udf7b\n\n### Interesting Story:\nIn the early 1900s, some car manufacturers offered a \u201cdriveaway service\u201d because people didn't know how to drive! They would send someone out to the customer\u2019s house to teach them\u2014the early days of customer service!\n\nHope this brought a smile to your day! If you want more car-related fun or need something else, just let me know! \ud83d\ude98\ud83d\udca8 \n\nTERMINATE",
#         "role": "user",
#         "name": "Customer_Engagement_Agent"
#     }
# ]
# --------------

print("\n\n\n\Costs per chat: >>>>>>>>>>>>>>>\n\n")
for chat_result in chat_results:
    print(f"{chat_result.cost}\n--------------")

##NOTES

# 1. Corner cases and relevance scenario for Agent
# A typical weak spot for GetnAI/LLM is not picking right scenarious. Such as I don't
# see why soliciting name and location via LLM (rather than letting a user use arbitraty strucuture)
# is a good idea. Essentialy you get a fixed 2 turn dialog with LLN where a user can input anything,
# there's no input validation, the flow will proceed even if user in the 2 messages asked about Cosmos
# and didn't tell anythin about his/her name and location. Why pick (1) LLM for the scenario
# which is better handled via form input and (2) why not cover corner cases (explain, might even skip code)
# and assume (as it nevener happens in real life) that user will behave - no guardrails and practicality
# covered in Task 1/Chat 1
#
# 2. Why agents?
# At first it was not clear why have 3 different agents to handle a single conversatio with the user
#
# 3. Crew.ai resemblane
# Though latter it became clear that via agents, chats and initiate_chats() you get what
# Crewai calls agents, tasks and crew.kickoff - conceptualu it is the same chain of prompts
# with one chat/task oputput provided as context to the next chat/task. And Autogen's
# sender and recipient fields control what is called task assignments and human in the loop
# in crewai.
# That's by the way what I liked about creai -  a clear and reasonable abstraction, while
# in Autogen it is too conceptual/abstract, hence the #2 confusion (Why agents?) - that makes
# Autogen more versatile and customizable, yet sometimes confuson with steeper learning curve
