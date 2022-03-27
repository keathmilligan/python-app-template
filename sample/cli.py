"""
Sample App Command-Line Interface
"""

import click
from .biz import my_func


@click.command()
@click.option("-a", "--alpha", default="avalue", help="Option A.")
@click.option("-b", "--beta", default="bvalue", help="Option B.")
def cli(alpha, beta):
    """
    Command-line example
    """
    click.echo("Option A: ", nl=False)
    click.secho(alpha, fg="red", bold=True, nl=False)
    click.echo(" Option B: ", nl=False)
    click.secho(beta, fg="blue", bold=True)
    result = my_func(alpha, beta)
    click.echo("Result: ", nl=False)
    click.secho(result, fg="bright_white", bg="green", bold=True)
