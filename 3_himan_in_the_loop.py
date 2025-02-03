import asyncio
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.base import Handoff
from autogen_agentchat.conditions import TextMentionTermination, HandoffTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from client import get_azure_client


async def main():
    model_client = get_azure_client()

    # print("\n\033[1;34mType APPROVE or provide feedback\033[0m\n\n")
    # # Create the agents.
    # assistant = AssistantAgent("assistant", model_client=model_client)
    # user_proxy = UserProxyAgent(
    #     "user_proxy", input_func=input
    # )  # Use input() to get user input from console.

    # # Create the termination condition which will end the conversation when the user says "APPROVE".
    # termination = TextMentionTermination("APPROVE")

    # # Create the team.
    # team = RoundRobinGroupChat(
    #     [assistant, user_proxy], termination_condition=termination
    # )

    # # Run the conversation and stream to the console.
    # stream = team.run_stream(task="Write a 4-line poem about the ocean.")
    # # Use asyncio.run(...) when running in a script.
    # await Console(stream)

    # print("\n\033[1;34mUser Input after termination\033[0m\n\n")

    # print("\n\033[1;34mMAX Turns 4\033[0m\n\n")

    # assistant = AssistantAgent("assistant", model_client=model_client)
    # # Create the team setting a maximum number of turns to 1.
    # team = RoundRobinGroupChat([assistant], max_turns=1)

    # task = "Write a 4-line poem about the ocean."
    # while True:
    #     # Run the conversation and stream to the console.
    #     stream = team.run_stream(task=task)
    #     # Use asyncio.run(...) when running in a script.
    #     await Console(stream)
    #     # Get the user response.
    #     task = input("Enter your feedback (type 'exit' to leave): ")
    #     if task.lower().strip() == "exit":
    #         break

    # Termination Conditions
    print("\n\n\nTermination Conditions\n\n\n")

    # Create a lazy assistant agent that always hands off to the user.
    lazy_agent = AssistantAgent(
        "lazy_assistant",
        model_client=model_client,
        handoffs=[Handoff(target="user", message="Transfer to user.")],
        system_message="If you cannot complete the task, transfer to user. Otherwise, when finished, respond with 'TERMINATE'.",
    )

    # Define a termination condition that checks for handoff messages.
    handoff_termination = HandoffTermination(target="user")
    # Define a termination condition that checks for a specific text mention.
    text_termination = TextMentionTermination("TERMINATE")

    # Create a single-agent team with the lazy assistant and both termination conditions.
    lazy_agent_team = RoundRobinGroupChat(
        [lazy_agent], termination_condition=handoff_termination | text_termination
    )

    # Run the team and stream to the console.
    task = "What is the weather in New York?"
    await Console(lazy_agent_team.run_stream(task=task))


if __name__ == "__main__":
    asyncio.run(main())
