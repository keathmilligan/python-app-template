Python Application Project Template
===================================

This repo provides a standardized template for Python application projects.

> This template is intended for general Python applications such as a command-line script or utility. If you are looking for a template for a shared library or framework project that you intend to publish to a public or private repository, see the [Python Package Boilerplate](https://github.com/keathmilligan/python-boilerplate) instead. For web applications and services, see [Flask Quick Start](https://github.com/keathmilligan/flask-quickstart).

Features:
* Predictable installation and package management with [Pipenv](https://pipenv.pypa.io/en/latest/).
* PyTest unit-test support
* PyLint and Black
* An [.editorconfig](http://editorconfig.org/) file
* Command-line argument parsing and color output support with [Click](https://click.palletsprojects.com/en/8.0.x/)

## Getting Started

This template uses [pipenv](https://pipenv.pypa.io/en/latest/) to manage dependencies and its virtual environment. You will need to install it if you do not already have it.

### Using the template

To use the template, click the **Use this template** button in the [Github repository](https://github.com/keathmilligan/python-app-template) to create a new project using this code as a basis. Alternatively, you can clone the repository locally.

### Install dependencies

> The template currently expects Python 3.10, if you need to use an older version, you will need to modify the `Pipfile`.

Use [pipenv](https://pipenv.pypa.io/en/latest/) to create a virtual environment and install the dependencies:

```
pipenv install --dev
```

The `--dev` option will also install the optional development dependencies such as `pylint` and `pytest`.

## Running

```
pipenv run python -m sample --help
```

This will display the application's help message.

Run with default args:

```
pipenv run python -m sample
```

![sample output](/docs/images/output.png)

## Testing

```
pipenv run pytest
```

## Adding command-line arguments and options

See `sample/cli.py` for an example command argument processor:

```python
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
```

This processor will be used when the `sample` package is invoked as a command (as above). Refer to the [Click documentation](https://click.palletsprojects.com/en/8.0.x/) for info on adding your own options and command line arguments.
