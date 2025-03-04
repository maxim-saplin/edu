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
    radio = mo.ui.radio(options=models, value=hf_model)
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

    r = "No results from the agent"

    if tool_start.value:
        agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=MODEL)
        r = agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")
    return CodeAgent, DuckDuckGoSearchTool, agent, r


@app.cell
def _(mo, r):
    if isinstance(r, list):
        result = "\n".join(str(item) for item in r)
    else:
        result = str(r)
    mo.md(result)
    return (result,)


@app.cell
def _(mo):
    mo.md(r"""## Custom Tool""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
