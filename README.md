# AI Agentic Design Patterns with AutoGen

Following the course at https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/

## Lesson 1: Multi-Agent Conversation and Stand-up Comedy

Using llm_config to set up LLM with Azure, basic 1-to-1 conversation between agents (messages of one LLM as sent us 'role:user' to another), printing cost, whole dialog (as OpenAI API JSON), summarizing chat. Trying 2 termination strategis: number of turns and stop phrase. Stop phrase turned to be chellenging, by default was endless, tried to steer conversation with updated prompts (the example on DL might have used different LLM, GPT 3.5, I used 4o Mini), sometimes the dialogs appeared a bit awkward.

(Note, tried using AI to generate this not based on comments in source file, eventually I have written it 100% maually, not taking anything from AI :)

## Lesson 2: Sequential Chats and Customer Onboarding

The lesson simulates a 3-step onboarding process using multiple agents:
1. Personal Information Agent: Collects name and location.
2. Topic Preference Agent: Gathers interests. Uses a lambda function for termination detection.
3. Engagement Agent: Delivers engaging content based on user info.

Had cognitive dissonance when 3 agents were supposed to ask 3 questions (name, location, interests). An agent in my head is an analog to a person, in this case it also seemed that we are automating customer support case which will typically be handled by a single human operator. Additioonally even witout agents this case perfectly fitst single multi-turn dialog with a single system message (e.g. you are a support specialist helping with onboparding etc.). All of that makes the example a bit superficial. Latter it became clear that agents and chats represented what creai calls agents and tasks - and this gives crewai an edge as it is useing relevant and meaningful contepts (and btw a single agentr will be OK to run 3 tasks in sequence).

- Adjusted agent names to avoid API errors
- Three distinct agents and chats are similar to Crew.ai's agents and task structure. initiate_chats() = crew.kickoff()
- The approach mirrors Crew.ai's chaining of tasks, but with more abstract and customizable elements.
- Non-typed dictionaries and magic strings are used, raising concerns about error-prone code.
- No input validation, no dicsussion (in learnin matgerials) of corner cases/guidertails
    - The floow can be broken any moment via arbitrary user input
- The whole example is a bit superficial, smells as irrelevant/is not grounded on the strengths of LLMs
    - From a UX standpoint asking for name/location via an agent rather than a validation form is awkward. It's kust like using a coinversational UI to pick the best color (asking to type in the color) of a product rather than showing a number of tiles with product pictures and asking to click the one user likes

## Lesson 3: Reflection and Blogpost Writing

This lesson explores the collaborative refinement of content using multiple agents:
1. Writer Agent: Crafts an initial blog post about DeepLearning.AI.
2. Critic Agent: Provides feedback to enhance the blog post.
3. Nested Reviewers: Includes SEO, Legal, and Ethics reviewers, each offering specialized insights.
4. Meta Reviewer: Aggregates all feedback to provide final suggestions.

- Agent Collaboration: Demonstrates iterative content improvement through agent teamwork.
- Nested Chats: Efficiently gathers diverse feedback, optimizing the review process.
- Abstraction Challenges: High-level abstractions in Autogen can obscure prompt flow control, complicating debugging.
- Practicality: While the pattern is intriguing, it may be rigid and not fully leverage LLM strengths. Simpler prompt chains might offer better control.

## Lesson 4: Tool Use and Conversational Chess

This lesson demonstrates the integration of tool use within a conversational chess game between AI agents:

1. Chess Board Initialization: Utilizes the chess library to set up and manage the game board.
2. Agent Roles:
   - Player White: A professional chess player agent.
   - Player Black: A beginner chess player agent.
3. Tool Registration: Functions like get_legal_moves and make_move are registered as tools for agents to interact with the chess board.
4. Game Dynamics:
   - Agents engage in nested chats to determine legal moves and execute them.
   - The game is animated using matplotlib to visualize moves.
5. LLMs lack awareness of the board state, relying solely on move history, which questions their ability to control the game effectively (might be changed to better utilize LLMs).

Challenges and Observations:
- The lesson highlights the limitations of LLMs in completing a chess game, with agents often making random moves after extended play.
- Emphasizes the need for better state management and error handling when LLMs suggest illegal moves.
- Demonstrates the potential of nested chats to provide guardrails and ensure valid gameplay.
- The example underscores how Gen AI tools are good to start something but struggle to finish, as even basic chess games were not completed after many turns.
- The exercise shows that while LLMs can initiate tasks, they may not excel in completing them without additional guidance.
- Highlights the importance of integrating real-time feedback and state awareness to improve AI performance in dynamic tasks.

## Comparison to Crewai

- I liked how Crewai had the streamlined concept of agents working in a team (a crew) on assigned task - something similar to what a Project Manager deal with in real life, familiar concept
- I also liked the ease of use, docs, web sites - all of the seemed more accomodating compared to Autogen
- Crewai doesn't support native tool call (i.e. using special kind of messages and relying on fine-tuned ability of LLM to respond with a reqeust for a tool call in a special message kind), crewai asks for tool directly in user prompt and parses the output in assistant natural language reply, while Autogen can use OpenAI's API for tool call and properly format tool description into the request
