import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import ExternalTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from client import get_azure_client
import pprint as pp


def pprint(obj):
    printer = pp.PrettyPrinter(indent=4)
    printer.pprint(obj)


async def main():
    model_client = get_azure_client()

    # Create the primary agent.
    writer_agent = AssistantAgent(
        "writer",
        model_client=model_client,
        system_message="You are a helpful AI assistant.",
    )

    # Create the critic agent.
    critic_agent = AssistantAgent(
        "critic",
        model_client=model_client,
        system_message="Provide constructive feedback. Respond with 'APPROVE' to when your feedbacks are addressed.",
    )

    # Define a termination condition that stops the task if the critic approves.
    text_termination = TextMentionTermination("APPROVE")

    # Create a team with the primary and critic agents.
    team = RoundRobinGroupChat(
        [writer_agent, critic_agent], termination_condition=text_termination
    )

    result = await team.run(task="Write a short poem about the fall season.")
    print("\n\033[1;34mRun a team in one go\033[0m\n\n")
    pprint(result)
    print("\n\033[1;34mDONE\033[0m\n\n")

    # Streaming, not to be confused with streaming in chats where you get token by token streaming while a message is being generated.
    # Here you get complete messages streamed when they are ready

    print("\n\033[1;34mRun a team with streaming\033[0m\n\n")
    await team.reset()  # Reset the team for a new task.
    message_count = 0
    async for message in team.run_stream(task="Write a short poem about the fall season."):  # type: ignore
        message_count += 1
        if isinstance(message, TaskResult):
            print("Stop Reason:", message.stop_reason)
        else:
            if message_count % 2 == 0:
                print("\033[1;32m")  # Green for even messages
            else:
                print("\033[1;31m")  # Red for odd messages
            pprint(message)
            print("\033[0m")  # Reset color
    print("\n\033[1;34mDONE\033[0m\n\n")

    print("\n\033[1;34mRun a team with streaming, output via Console\033[0m\n\n")
    await team.reset()  # Reset the team for a new task.
    await Console(
        team.run_stream(task="Write a short poem about the fall season.")
    )  # Stream the messages to the console.
    print("\n\033[1;34mDONE\033[0m\n\n")

    print("\n\033[1;34mRun a team with termination and resuming\033[0m\n\n")
    external_termination = ExternalTermination()
    team = RoundRobinGroupChat(
        [writer_agent, critic_agent],
        termination_condition=external_termination
        | text_termination,  # Use the bitwise OR operator to combine conditions.
    )

    # Run the team in a background task.
    run = asyncio.create_task(
        Console(team.run_stream(task="Write a short poem about the fall season."))
    )

    # Wait for some time.
    await asyncio.sleep(0.1)

    # Stop the team.
    external_termination.set()

    # Wait for the team to finish.
    await run
    await Console(team.run_stream())  # Resume the team to continue the last task.
    await Console(
        team.run_stream(task="将这首诗用中文唐诗风格写一遍。")
    )  # The new task is to translate the same poem to Chinese Tang-style poetry.
    print("\n\033[1;34mDONE\033[0m\n\n")

    print("\n\033[1;34mRun a team with termination\033[0m\n\n")

    # Create a cancellation token.
    cancellation_token = CancellationToken()

    # Use another coroutine to run the team.
    run = asyncio.create_task(
        team.run(
            task="Translate the poem to Spanish.",
            cancellation_token=cancellation_token,
        )
    )

    # Cancel the run.
    cancellation_token.cancel()

    try:
        result = await run  # This will raise a CancelledError.
    except asyncio.CancelledError:
        print("Task was cancelled.")
    print("\n\033[1;34mDONE\033[0m\n\n")


if __name__ == "__main__":
    asyncio.run(main())
