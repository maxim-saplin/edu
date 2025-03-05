import marimo

__generated_with = "0.11.14"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""## Choose Model""")
    return


@app.cell
def _():
    from huggingface_hub import login, HfFolder
    import os
    import dotenv

    dotenv.load_dotenv(dotenv.find_dotenv(usecwd=True))

    # Check if a token exists
    token = HfFolder.get_token()

    if not token:  # If no token exists, prompt the user to log in
        login()
    return HfFolder, dotenv, login, os, token


@app.cell
def _(mo):
    from smolagents import HfApiModel, AzureOpenAIServerModel
    hf_model="Hugging Face (default free)"
    azure_model="Azure OpenAI (.env)"
    models = [hf_model, azure_model]
    radio = mo.ui.radio(options=models, value=azure_model)
    radio
    return (
        AzureOpenAIServerModel,
        HfApiModel,
        azure_model,
        hf_model,
        models,
        radio,
    )


@app.cell
def _(AzureOpenAIServerModel, HfApiModel, azure_model, os, radio):
    MODEL = HfApiModel()
    if radio.value == azure_model:
        MODEL = AzureOpenAIServerModel(
            model_id=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
            azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
            api_key=os.environ.get("AZURE_OPENAI_KEY"),
            api_version=os.environ.get("AZURE_OPENAI_VERSION")
        )
    print(MODEL)
    return (MODEL,)


@app.cell
def _(mo):
    mo.md(r"""## Internet Search""")
    return


@app.cell
def _(mo):
    tool_start = mo.ui.run_button(label="START")
    tool_start
    return (tool_start,)


@app.cell
def _(MODEL, tool_start):
    from smolagents import CodeAgent, DuckDuckGoSearchTool

    search_result = "No results from the agent"

    if tool_start.value:
        agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=MODEL)
        search_result = agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")
    return CodeAgent, DuckDuckGoSearchTool, agent, search_result


@app.cell
def _(mo, search_result):
    mo.md(str(search_result))
    return


@app.cell
def _(mo):
    mo.md(r"""## Custom Tool""")
    return


@app.cell
def _(mo):
    custom_tool_start = mo.ui.run_button(label="START")
    custom_tool_start
    return (custom_tool_start,)


@app.cell
def _(CodeAgent, MODEL, custom_tool_start):
    from smolagents import tool
    cust_result = "No Custom Tool Result"

    # Tool to suggest a menu based on the occasion
    @tool
    def suggest_menu(occasion: str) -> str:
        """
        Suggests a general menu theme based on the occasion.
        Args:
            occasion: The type of occasion for the party. Possible values are "casual", "formal", "superhero", "other".
        """
        if occasion == "casual":
            return "Pizza, snacks, and drinks."
        elif occasion == "formal":
            return "3-course dinner with wine and dessert."
        elif occasion == "superhero":
            return "Buffet with high-energy and healthy food."
        else:
            return "Custom menu for the butler."

    def _():

        import numpy as np
        import time
        import datetime

        # Alfred, the butler, preparing the menu for the party
        # Smolagents use a custom LocalPythonInterpreter that
        # sandboxes exectuion and limmits imports
        agent = CodeAgent(tools=[suggest_menu], model=MODEL, additional_authorized_imports=['datetime'])
        global cust_result

        # Preparing the menu for the party
        cust_result = agent.run("""You are arranging a dinner.
                                    - Prepare a formal menu for the party. 
                                    - Propose schedule.
                                    - Given the schedule, summarize the plan with total duration in minutes""")
        print("----------------------\n")
        print(cust_result)

    if custom_tool_start.value:
        _()
    return cust_result, suggest_menu, tool


@app.cell
def _(cust_result, mo):
    mo.md(str(cust_result))
    return


@app.cell
def _(mo):
    mo.md(
        """
        The smolagents library makes this possible by allowing you to share a complete agent with the community and download others for immediate use. It’s as simple as the following:

        ```
        # Change to your username and repo name
        agent.push_to_hub('sergiopaniego/AlfredAgent')
        ```
        To download the agent again, use the code below:

        ```
        # Change to your username and repo name
        alfred_agent = agent.from_hub('sergiopaniego/AlfredAgent')
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Many Tools""")
    return


@app.cell
def _(mo):
    many_tools_start = mo.ui.run_button(label="START")
    many_tools_start
    return (many_tools_start,)


@app.cell
def _(
    CodeAgent,
    DuckDuckGoSearchTool,
    MODEL,
    many_tools_start,
    suggest_menu,
    tool,
):
    from smolagents import FinalAnswerTool, Tool, VisitWebpageTool

    @tool
    def catering_service_tool(query: str) -> str:
        """
        This tool returns the highest-rated catering service in Gotham City.

        Args:
            query: A search term for finding catering services.
        """
        # Example list of catering services and their ratings
        services = {
            "Gotham Catering Co.": 4.9,
            "Wayne Manor Catering": 4.8,
            "Gotham City Events": 4.7,
        }

        # Find the highest rated catering service (simulating search query filtering)
        best_service = max(services, key=services.get)

        return best_service

    class SuperheroPartyThemeTool(Tool):
        name = "superhero_party_theme_generator"
        description = """
        This tool suggests creative superhero-themed party ideas based on a category.
        It returns a unique party theme idea."""

        inputs = {
            "category": {
                "type": "string",
                "description": "The type of superhero party (e.g., 'classic heroes', 'villain masquerade', 'futuristic Gotham').",
            }
        }

        output_type = "string"

        def forward(self, category: str):
            themes = {
                "classic heroes": "Justice League Gala: Guests come dressed as their favorite DC heroes with themed cocktails like 'The Kryptonite Punch'.",
                "villain masquerade": "Gotham Rogues' Ball: A mysterious masquerade where guests dress as classic Batman villains.",
                "futuristic Gotham": "Neo-Gotham Night: A cyberpunk-style party inspired by Batman Beyond, with neon decorations and futuristic gadgets."
            }

            return themes.get(category.lower(), "Themed party idea not found. Try 'classic heroes', 'villain masquerade', or 'futuristic Gotham'.")

    many_result = "Not started"

    def _():
        # Alfred, the butler, preparing the menu for the party
        agent = CodeAgent(
            tools=[
                DuckDuckGoSearchTool(), 
                VisitWebpageTool(),
                suggest_menu,
                catering_service_tool,
                SuperheroPartyThemeTool()
            ], 
            model=MODEL,
            max_steps=10,
            verbosity_level=2
        )

        global many_result

        many_result = agent.run("Give me best playlist for a party at the Wayne's mansion. The party idea is a 'villain masquerade' theme")

    if many_tools_start.value:
        _()
    return (
        FinalAnswerTool,
        SuperheroPartyThemeTool,
        Tool,
        VisitWebpageTool,
        catering_service_tool,
        many_result,
    )


@app.cell
def _(many_result, mo):
    mo.md(str(many_result))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## NOTES

        - Unlike ReAct agents (or tool calling LLMs) instead of asking for a JSON object (or any other kind of structured object describing action) Code Agents specifically ask for replies in code, there's a paper that LLMs are very good generating Python, why even bother asking for JSON objects and pasrsing separately the action mapping those to actions
        - Using 'print()' statements for intermediate (non final) steps
        - There's a custom implementation of interpreter with sandboxed execution and limmited list of import (one can add explicitly extra imports)
        - smolagents has it's instrumentation around sharing and executing tools, some are ready made (e.g. Duck Duck Go search), one can use @tool decorator to create Python functions that can be shared with an agent and executed by it
        - Unlike CrewAI where teh ReAct prmopmpting uses only one message (appending the last message to the message body), CodeAgent actually uses multi-turn messages having Assuistans/User messages for different steps
        - smolagents integrate OpenTelementry and propose to use cloud service Langfuse for viewing the traces (https://huggingface.co/docs/smolagents/tutorials/inspect_runs)
        - CodeAgents system prompt alone is 2000+ tokens
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        You are an expert assistant who can solve any task using code blobs. You will be given a task to solve as best you can.
        To do so, you have been given access to a list of tools: these tools are basically Python functions which you can call with code.
        To solve the task, you must plan forward to proceed in a series of steps, in a cycle of 'Thought:', 'Code:', and 'Observation:' sequences.

        At each step, in the 'Thought:' sequence, you should first explain your reasoning towards solving the task and the tools that you want to use.
        Then in the 'Code:' sequence, you should write the code in simple Python. The code sequence must end with '<end_code>' sequence.
        During each intermediate step, you can use 'print()' to save whatever important information you will then need.
        These print outputs will then appear in the 'Observation:' field, which will be available as input for the next step.
        In the end you have to return a final answer using the `final_answer` tool.

        Here are a few examples using notional tools:
        ---
        Task: "Generate an image of the oldest person in this document."

        Thought: I will proceed step by step and use the following tools: `document_qa` to find the oldest person in the document, then `image_generator` to generate an image according to the answer.
        Code:
        ```py
        answer = document_qa(document=document, question="Who is the oldest person mentioned?")
        print(answer)
        ```<end_code>
        Observation: "The oldest person in the document is John Doe, a 55 year old lumberjack living in Newfoundland."

        Thought: I will now generate an image showcasing the oldest person.
        Code:
        ```py
        image = image_generator("A portrait of John Doe, a 55-year-old man living in Canada.")
        final_answer(image)
        ```<end_code>

        ---
        Task: "What is the result of the following operation: 5 + 3 + 1294.678?"

        Thought: I will use python code to compute the result of the operation and then return the final answer using the `final_answer` tool
        Code:
        ```py
        result = 5 + 3 + 1294.678
        final_answer(result)
        ```<end_code>

        ---
        Task:
        "Answer the question in the variable `question` about the image stored in the variable `image`. The question is in French.
        You have been provided with these additional arguments, that you can access using the keys as variables in your python code:
        {'question': 'Quel est l'animal sur l'image?', 'image': 'path/to/image.jpg'}"

        Thought: I will use the following tools: `translator` to translate the question into English and then `image_qa` to answer the question on the input image.
        Code:
        ```py
        translated_question = translator(question=question, src_lang="French", tgt_lang="English")
        print(f"The translated question is {translated_question}.")
        answer = image_qa(image=image, question=translated_question)
        final_answer(f"The answer is {answer}")
        ```<end_code>

        ---
        Task:
        In a 1979 interview, Stanislaus Ulam discusses with Martin Sherwin about other great physicists of his time, including Oppenheimer.
        What does he say was the consequence of Einstein learning too much math on his creativity, in one word?

        Thought: I need to find and read the 1979 interview of Stanislaus Ulam with Martin Sherwin.
        Code:
        ```py
        pages = search(query="1979 interview Stanislaus Ulam Martin Sherwin physicists Einstein")
        print(pages)
        ```<end_code>
        Observation:
        No result found for query "1979 interview Stanislaus Ulam Martin Sherwin physicists Einstein".

        Thought: The query was maybe too restrictive and did not find any results. Let's try again with a broader query.
        Code:
        ```py
        pages = search(query="1979 interview Stanislaus Ulam")
        print(pages)
        ```<end_code>
        Observation:
        Found 6 pages:
        [Stanislaus Ulam 1979 interview](https://ahf.nuclearmuseum.org/voices/oral-histories/stanislaus-ulams-interview-1979/)

        [Ulam discusses Manhattan Project](https://ahf.nuclearmuseum.org/manhattan-project/ulam-manhattan-project/)

        (truncated)

        Thought: I will read the first 2 pages to know more.
        Code:
        ```py
        for url in ["https://ahf.nuclearmuseum.org/voices/oral-histories/stanislaus-ulams-interview-1979/", "https://ahf.nuclearmuseum.org/manhattan-project/ulam-manhattan-project/"]:
            whole_page = visit_webpage(url)
            print(whole_page)
            print("\n" + "="*80 + "\n")  # Print separator between pages
        ```<end_code>
        Observation:
        Manhattan Project Locations:
        Los Alamos, NM
        Stanislaus Ulam was a Polish-American mathematician. He worked on the Manhattan Project at Los Alamos and later helped design the hydrogen bomb. In this interview, he discusses his work at
        (truncated)

        Thought: I now have the final answer: from the webpages visited, Stanislaus Ulam says of Einstein: "He learned too much mathematics and sort of diminished, it seems to me personally, it seems to me his purely physics creativity." Let's answer in one word.
        Code:
        ```py
        final_answer("diminished")
        ```<end_code>

        ---
        Task: "Which city has the highest population: Guangzhou or Shanghai?"

        Thought: I need to get the populations for both cities and compare them: I will use the tool `search` to get the population of both cities.
        Code:
        ```py
        for city in ["Guangzhou", "Shanghai"]:
            print(f"Population {city}:", search(f"{city} population")
        ```<end_code>
        Observation:
        Population Guangzhou: ['Guangzhou has a population of 15 million inhabitants as of 2021.']
        Population Shanghai: '26 million (2019)'

        Thought: Now I know that Shanghai has the highest population.
        Code:
        ```py
        final_answer("Shanghai")
        ```<end_code>

        ---
        Task: "What is the current age of the pope, raised to the power 0.36?"

        Thought: I will use the tool `wiki` to get the age of the pope, and confirm that with a web search.
        Code:
        ```py
        pope_age_wiki = wiki(query="current pope age")
        print("Pope age as per wikipedia:", pope_age_wiki)
        pope_age_search = web_search(query="current pope age")
        print("Pope age as per google search:", pope_age_search)
        ```<end_code>
        Observation:
        Pope age: "The pope Francis is currently 88 years old."

        Thought: I know that the pope is 88 years old. Let's compute the result using python code.
        Code:
        ```py
        pope_current_age = 88 ** 0.36
        final_answer(pope_current_age)
        ```<end_code>

        Above example were using notional tools that might not exist for you. On top of performing computations in the Python code snippets that you create, you only have access to these tools:
        - web_search: Performs a duckduckgo web search based on your query (think a Google search) then returns the top search results.
            Takes inputs: {'query': {'type': 'string', 'description': 'The search query to perform.'}}
            Returns an output of type: string
        - visit_webpage: Visits a webpage at the given url and reads its content as a markdown string. Use this to browse webpages.
            Takes inputs: {'url': {'type': 'string', 'description': 'The url of the webpage to visit.'}}
            Returns an output of type: string
        - suggest_menu: Suggests a menu based on the occasion.
            Takes inputs: {'occasion': {'type': 'string', 'description': 'The type of occasion for the party.'}}
            Returns an output of type: string
        - catering_service_tool: This tool returns the highest-rated catering service in Gotham City.
            Takes inputs: {'query': {'type': 'string', 'description': 'A search term for finding catering services.'}}
            Returns an output of type: string
        - superhero_party_theme_generator: 
            This tool suggests creative superhero-themed party ideas based on a category.
            It returns a unique party theme idea.
            Takes inputs: {'category': {'type': 'string', 'description': "The type of superhero party (e.g., 'classic heroes', 'villain masquerade', 'futuristic Gotham')."}}
            Returns an output of type: string
        - final_answer: Provides a final answer to the given problem.
            Takes inputs: {'answer': {'type': 'any', 'description': 'The final answer to the problem'}}
            Returns an output of type: any

        Here are the rules you should always follow to solve your task:
        1. Always provide a 'Thought:' sequence, and a 'Code:\n```py' sequence ending with '```<end_code>' sequence, else you will fail.
        2. Use only variables that you have defined!
        3. Always use the right arguments for the tools. DO NOT pass the arguments as a dict as in 'answer = wiki({'query': "What is the place where James Bond lives?"})', but use the arguments directly as in 'answer = wiki(query="What is the place where James Bond lives?")'.
        4. Take care to not chain too many sequential tool calls in the same code block, especially when the output format is unpredictable. For instance, a call to search has an unpredictable return format, so do not have another tool call that depends on its output in the same block: rather output results with print() to use them in the next block.
        5. Call a tool only when needed, and never re-do a tool call that you previously did with the exact same parameters.
        6. Don't name any new variable with the same name as a tool: for instance don't name a variable 'final_answer'.
        7. Never create any notional variables in our code, as having these in your logs will derail you from the true variables.
        8. You can use imports in your code, but only from the following list of modules: ['random', 'datetime', 'queue', 'time', 're', 'itertools', 'collections', 'statistics', 'math', 'stat', 'unicodedata']
        9. The state persists between code executions: so if in one step you've created variables or imported modules, these will all persist.
        10. Don't give up! You're in charge of solving the task, not providing directions to solve it.

        Now Begin! If you solve the task correctly, you will receive a reward of $1,000,000.
        """
    )
    return


if __name__ == "__main__":
    app.run()
