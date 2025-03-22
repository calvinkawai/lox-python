"""CLI interface for lox_python project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
from lox_python.lox import Lox


def main(*args):  # pragma: no cover
    """
    The main function executes on commands:
    `python -m lox_python` and `$ lox_python `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    if len(args) > 1:
        print("Usage: python -m lox_python [script]")
    elif len(args) == 1:
        Lox.run_file(args[0])
    else:
        Lox.run_prompt()
