import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from client import get_azure_client


async def main():
    model_client = get_azure_client()

    assistant_agent = AssistantAgent(
        name="assistant_agent",
        system_message="You are a helpful assistant",
        model_client=model_client,
    )

    response = await assistant_agent.on_messages(
        [TextMessage(content="Write a 3 line poem on lake tangayika", source="user")],
        CancellationToken(),
    )
    print(response.chat_message.content)

    agent_state = await assistant_agent.save_state()
    print(agent_state)

    new_assistant_agent = AssistantAgent(
        name="assistant_agent",
        system_message="You are a helpful assistant",
        model_client=model_client,
    )
    await new_assistant_agent.load_state(agent_state)

    response = await new_assistant_agent.on_messages(
        [
            TextMessage(
                content="What was the last line of the previous poem you wrote",
                source="user",
            )
        ],
        CancellationToken(),
    )
    print(response.chat_message.content)


if __name__ == "__main__":
    asyncio.run(main())
