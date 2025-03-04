import marimo

__generated_with = "0.11.14"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""Login to HF (JIC)""")
    return


@app.cell
def _():
    from huggingface_hub import login

    login()
    return (login,)


if __name__ == "__main__":
    app.run()
