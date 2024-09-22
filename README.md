# AI Agentic Design Patterns with AutoGen

Following the course at https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/

## Lesson 1: Multi-Agent Conversation and Stand-up Comedy

Using llm_config to set up LLM with Azure, basic 1-to-1 conversation between agents (messages of one LLM as sent us 'role:user' to another), printing cost, whole dialog (as OpenAI API JSON), summarizing chat. Trying 2 termination strategis: number of turns and stop phrase. Stop phrase turned to be chellenging, by default was endless, tried to steer conversation with updated prompts (the example on DL might have used different LLM, GPT 3.5, I used 4o Mini), sometimes the dialogs appeared a bit awkward.

(Note, tried using AI to generate this not based on comments in source file, eventually I have written it 100% maually, not taking anything from AI :)

## Lesson 2: Sequential Chats and Customer Onboarding

The lesson simulates a 3-step onboarding process using multiple agents:
1. **Personal Information Agent**: Collects name and location.
2. **Topic Preference Agent**: Gathers interests. Uses a lambda function for termination detection.
3. **Engagement Agent**: Delivers engaging content based on user info.

- Adjusted agent names to avoid API errors
- Three distinct agents and chats are similar to Crew.ai's agents and task structure. initiate_chats() = crew.kickoff()
- The approach mirrors Crew.ai's chaining of tasks, but with more abstract and customizable elements.
- Non-typed dictionaries and magic strings are used, raising concerns about error-prone code.
- No input validation, no dicsussion (in learnin matgerials) of corner cases/guidertails
    - The floow can be broken any moment via arbitrary user input
- The whole example is a bit superficial, smells as irrelevant/is not grounded on the strengths of LLMs
    - From a UX standpoint asking for name/location via an agent rather than a validation form is awkward. It's kust like using a coinversational UI to pick the best color (asking to type in the color) of a product rather than showing a number of tiles with product pictures and asking to click the one user likes
