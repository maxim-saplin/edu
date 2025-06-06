Practice/examples from Huggingface's Agents Course

- https://huggingface.co/learn/agents-course/unit2/smolagents/introduction

1. Activate venv
2. `pip install -r requirements.txt`

Lessons 1 - 5 use Smolagents, Lesson 6 is LlamaIndex, Lesson 7 is LangGraph

## Lesson 1 - Agents that use Code

- Unlike ReAct agents (or tool calling LLMs) instead of asking for a JSON object (or any other kind of structured object describing action) Code Agents specifically ask for replies in code, there's a paper that LLMs are very good generating Python, why even bother asking for JSON objects and pasrsing separately the action mapping those to actions
- Using 'print()' statements for intermediate (non final) steps
- There's a custom implementation of interpreter with sandboxed execution and limmited list of import (one can add explicitly extra imports)
- smolagents has it's instrumentation around sharing and executing tools, some are ready made (e.g. Duck Duck Go search), one can use @tool decorator to create Python functions that can be shared with an agent and executed by it
- Unlike CrewAI where teh ReAct prmopmpting uses only one message (appending the last message to the message body), CodeAgent actually uses multi-turn messages having Assuistans/User messages for different steps
- smolagents integrate OpenTelementry and propose to use cloud service Langfuse for viewing the traces (https://huggingface.co/docs/smolagents/tutorials/inspect_runs)
- CodeAgents system prompt alone is 2000+ tokens

## Lesson 2 - Writing actions as code snippets or JSON blobs

- ToolCallingAgent class relies or models native support for funtion/tool calling
- Otherwise seems similar to CodeAgent in terms of results, it just achived via a different approach
- System prompt is just 997 tokens - much better than CodeAgent

## Lesson 3 - Tools

- @tool atribute (easier) vs inheriting from Tool class
- The former relies on smolagents passing in docstring as tool descriotion to LLM, the latter one gives more finer grain control
- One can load tools from HF (as well as upload tools there), use HF spaces as tools and import LangChain tools

## Lesson 4 - RAG

- Perplexity in (almost) 10 lines of code - liked how easy it was it implement a bot that used 2 tools - web search and web visit
- Another sample relied on LangChain's tools for chunking and semanric search vi embeddings (BM25 rrtiever)

## Lesson 5 - Multi-Agent

- Liked how manager works and how visulationzation create an ACSCII graph of model dependency
- Setting agent.planning_interval to the number of steps at which planning prompt is inserted, i.e. smoll agent prompts the LLM to make a plan at this number of steps (starting 0)
- Yet authorized imports and code generation (even with GPT-4o) is not as flawless - had to make a number of attempts fighting to have all required imports, dependencies installed via pip, observing how agents struggled generating code that actually worked (e.g. multiple Error in code parsing:
Your code snippet is invalid, because the regex pattern ```(?:py|python)?\n(.*?)\n``` was not found in it. OR ode that didn't run)
- `manager_agent.python_executor.state["fig"]` was magical, didn't expect it'd build an interactive zoomable map with PoI. I used shorter prompt wiht no example of ho to plot data (the original prompt had code sample with "fig" var), LLM made the rigth code snippet with the assuned fig local var name (guess it's pretty common in training data)

## Lesson 6 - Vision model

- Nice end-to-end example with Selenium web driver controlling chrome and GPOT-4o using vision to decide on next steps
- Yet bot struggled closing pcookie pop-ups and never completed execution... Too much effort to little result to my liking

## Lesson 7 - LlamaIndex

- While LLama Index has the basic facilities for generating responses with LLMs it's key strngth seem to be the data extraction, indexing and processing via LLMs
- LLama hub has plenty of integrations
- LLM as a judge for quick RAG eval (FaithfulnessEvaluator, AnswerRelevancyEvaluator, CorrectnessEvaluator)
- Has own helpers for tools (define Pyhton func, pass it into LLM, get called, return results to LLM), can group tools in tools specs, supports callinmg MCP servers via McpToolSpec()
- Supports 3 kinds of agents: Function Calling Agents (for LLMs with native function calling), ReAct Agents (can work with any AI that does chat or text endpoint), Advanced Custom Agents (use more complex methods likeLLMCompiler or Chain-of-Abstraction)
- Support multi-agent systems and workflows

## Lesson 8 - LangGraph

- From the creators of LangChain, doesn't depend on LangChain
- Formalizes workflows as nodes (actions as python functions), edges (transtions to other nodes) and states


## Marimo

Tried Marimo (`marimo edit --watch 1_smolagents.py` ) with 1st lesson, unfortunate discoveries:
 - No debegging (breakpoints, traces, stepping into)
 - No clear way to store cell outputs to Git - found that Marimo uses a different approach - Auto-download (availble thropugh gerar icon at the top right). This way a snapshot will be saved to `__marimo__` folder
 - Suggests to use included web IDE in edit mode (it even has support for AI assisant), though it's inferior to VSCode experience, had issues switching between Web and VSCode when I wanted AI assistance, like Jupyter in this regard
 - Don't see why I need to mix Jupyter and Stremalit in Marimo which has 2 distinct modes - Notebooks (edit) and App (run)