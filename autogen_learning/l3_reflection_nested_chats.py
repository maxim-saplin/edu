# flake8: noqa: 266
import pprint
import autogen
from llm import get_llm_config

llm_config = get_llm_config()

## Writing a blogpost, 1-step

task = """
        Write a concise but engaging blogpost about
       DeepLearning.AI. Make sure the blogpost is
       within 100 words.
       """

# Not sure why AssitantAgent is used here, seems like the only difference
# from ConversableAgent used before is the presence of default system message
# which is overriden anyway - hence no pooint in introducing a different kind of agent
writer = autogen.AssistantAgent(
    name="Writer",
    system_message="You are a writer. You write engaging and concise "
    "blogpost (with title) on given topics. You must polish your "
    "writing based on the feedback you receive and give a refined "
    "version. Only return your final work without additional comments.",
    llm_config=llm_config,
)

# reply = writer.generate_reply(messages=[{"content": task, "role": "user"}])

# print(reply)

## Add Reflection

critic = autogen.AssistantAgent(
    name="Critic",
    is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
    llm_config=llm_config,
    # In this case we are mixing the role place and task definition
    # while with Writer it there's a separate message for task for Writer
    system_message="You are a critic. You review the work of "
    "the writer and provide constructive "
    "feedback to help improve the quality of the content.",
)

# That's how you make 2 LLMs collaborate/discuss the subject, Critic is the sender of the 1st message which is task
# Terminating on 2nd turn, since the last message comes froim writer, it is likely to contain one iteration
# on the blog post based on feedback provided from Ciritc:
#
# Writer {role: "system"}   - system message
#   <- 1st turn ->
# Critic {role: "user"}     - task
# Writer {role: "assitant"} - blog post
#   <- 2nd turn ->
# Critic {role: "user"}     - feedback
# Writer {role: "assitant"} - updated blog post

# res = critic.initiate_chat(
#     recipient=writer, message=task, max_turns=2, summary_method="last_msg"
# )

## Nested Chat

# Changing AssitantAgent to ConversableAgent
SEO_reviewer = autogen.ConversableAgent(
    name="SEO Reviewer",
    llm_config=llm_config,
    system_message="You are an SEO reviewer, known for "
    "your ability to optimize content for search engines, "
    "ensuring that it ranks well and attracts organic traffic. "
    "Make sure your suggestion is concise (within 3 bullet points), "
    "concrete and to the point. "
    "Begin the review by stating your role.",
)

legal_reviewer = autogen.ConversableAgent(
    name="Legal Reviewer",
    llm_config=llm_config,
    system_message="You are a legal reviewer, known for "
    "your ability to ensure that content is legally compliant "
    "and free from any potential legal issues. "
    "Make sure your suggestion is concise (within 3 bullet points), "
    "concrete and to the point. "
    "Begin the review by stating your role.",
)

ethics_reviewer = autogen.ConversableAgent(
    name="Ethics Reviewer",
    llm_config=llm_config,
    system_message="You are an ethics reviewer, known for "
    "your ability to ensure that content is ethically sound "
    "and free from any potential ethical issues. "
    "Make sure your suggestion is concise (within 3 bullet points), "
    "concrete and to the point. "
    "Begin the review by stating your role. ",
)

meta_reviewer = autogen.ConversableAgent(
    name="Meta Reviewer",
    llm_config=llm_config,
    system_message="You are a meta reviewer, you aggragate and review "
    "the work of other reviewers and give a final suggestion on the content.",
)

print("\n\n\n\n\n---------------------------------------\n\n\n\n\n")


# This is used as template generator to start each individual chat between Critic and the rest of the agents
# passing in Writer input into nested chats from the upper levels Critic<->Writer chat
def reflection_message(recipient, messages, sender, config):
    return f"""Review the following content. 
            \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}"""


# Nested chats are initiated via Critic, exit contidion is one turn
# Turn off "summary_method": "reflection_with_llm" as it doesn't yield any Context to the meta reviewer
# while in DL course the meta reviewer received a complete list of JSON objects - seems like a bug
# (I used version 0.3.0 of Autogen and GPT-4o mini, while DL had 0.2.25 and GPT 3.5)
review_chats = [
    {
        "recipient": SEO_reviewer,
        "message": reflection_message,
        # "summary_method": "reflection_with_llm",
        # Get the structured output via "NL-to-Format (1st turn is terminated, 2nd turn summary processing whcih is converting Natural Language dialog (1st turn) to JSON)"
        # "summary_args": {
        #     "summary_prompt": "Return review as JSON object with following firlds:"
        #     "{'reviewer': '<your role>', 'review': '<your review>'}",
        # },
        "max_turns": 1,
    },
    {
        "recipient": legal_reviewer,
        "message": reflection_message,
        # "summary_method": "reflection_with_llm",
        # "summary_args": {
        #     "summary_prompt": "Return review as JSON object with following firlds:"
        #     "{'reviewer': '<your role>', 'review': '<your review>'}",
        # },
        "max_turns": 1,
    },
    {
        "recipient": ethics_reviewer,
        "message": reflection_message,
        # "summary_method": "reflection_with_llm",
        # "summary_args": {
        #     "summary_prompt": "Return review as JSON object with following firlds:"
        #     "{'reviewer': '<your role>', 'review': '<your review>'}",
        # },
        "max_turns": 1,
    },
    # For some reasons only the lat chat received as a context the resuls (last messages) from the above chats
    # Not sure why, seems like some implicit converntion not reflected anywhere in the docs
    # Better be excplicitly controlled via params to avoid this magic conventions and tacit knowledge
    {
        "recipient": meta_reviewer,
        "message": "Aggregrate feedback from all reviewers and give final suggestions on the writing.",
        "max_turns": 1,
    },
]

critic.register_nested_chats(
    review_chats,
    trigger=writer,
)

chat_result = critic.initiate_chat(
    recipient=writer, message=task, max_turns=2, summary_method="last_msg"
)

# This is the result of the chat chain with the last message saved to summary (summary_method="last_msg")
# containing the meta reviwers last message
print(chat_result.summary)

print("\n\n\n\n\n---------------------------------------\n\n\n\n\n")

# This one onl prints the top level chat/dict of LLM conversation log
# Not sure how to show the history of nested chats
# pprint.pprint(chat_result.chat_history)

## Notes
# Overal with nested chats we get a top level chat with 2 turns between Critic and writer (4 messages),
# Before initiating the 2nd turn the Critic starts 4 child chats aggregating feedback from 4 different agents
# and then using it as the 2nd message to the writer asking it to make another attempt
# This looks like an interesting pattern where you can launch a subchain of prompts doing processing of master chain's mssages,
# also aggergsting a review from 4 agents from a nested chat makes sense as it may save on tokens
# and not confuse the writer with abundance of input words.
# Yet the demonstration is quite rigid prompt chain, not a versatile self-managed collective of agents (yet again inflated Gen AI expectations).
# Anyways not sure if Autogen brings much value here, still missing the control over prompts and their flow (the LangChain controversy is relevant here),
# Autogen might be giving to much abstractions which stay in a way and do not help with debugging (see the llm summarization commented out
# in nested chats due to bugs). I still fell that for such cases (up until lesson 3) Autogen doesn't give much value,
# simplictic prompt chains bakcreferencing previous chains with minimal LLM libraries are better and give more visibility and controler over prompts,
# e.g. https://gist.github.com/disler/d51d7e37c3e5f8d277d8e0a71f4a1d2e
# (TODO - try recreating this sample with prompt chain as in the link, see how it compares)
