Practice/examples from Huggingface's Agents Course

- https://huggingface.co/learn/agents-course/unit2/smolagents/introduction

1. Activate venv
2. `pip install -r requirements.txt`

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

## Notes

- Tried Marimo (`marimo edit --watch 1_smolagents.py` ) with 1st lesson, unfortunate discoveries:
    - No debegging (breakpoints, traces, stepping into)
    - No clear way to store cell outputs to Git - found that Marimo uses a different approach - Auto-download (availble thropugh gerar icon at the top right). This way a snapshot will be saved to `__marimo__` folder
    - Don't see why I need to mix Jupyter and Stremalit in Marimo which has 2 distinct modes - Notebooks (edit) and App (run) 