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
        Suggests a menu based on the occasion.
        Args:
            occasion: The type of occasion for the party.
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
        cust_result = agent.run("Prepare a formal menu for the party. Break it down into schedule")
        print("----------------------\n")
        print(cust_result)

    if custom_tool_start.value:
        _()
    return cust_result, suggest_menu, tool


@app.cell
def _(cust_result, mo):
    mo.md(str(cust_result))
    return


if __name__ == "__main__":
    app.run()
