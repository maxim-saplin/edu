# AI Agentic Design Patterns with AutoGen

Following the course at https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/

## Lesson 1: Multi-Agent Conversation and Stand-up Comedy

Using llm_config to set up LLM with Azure, basic 1-to-1 conversation between agents (messages of one LLM as sent us 'role:user' to another), printing cost, whole dialog (as OpenAI API JSON), summarizing chat. Trying 2 termination strategis: number of turns and stop phrase. Stop phrase turned to be chellenging, by default was endless, tried to steer conversation with updated prompts (the example on DL might have used different LLM, GPT 3.5?, I used 4o Mini), sometimes the dialogs appeared a bit awkward.