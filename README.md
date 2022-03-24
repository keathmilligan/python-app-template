Python Application Project Template
===================================

This repo provides a standardized template for Python application projects.

> This template is intended for general Python applications such as a command-line script or utility. If you are looking for a template for a shared library or framework project that you intend to publish to a public or private repository, see the [Python Package Boilerplate](https://github.com/keathmilligan/python-boilerplate) instead. For web applications and services, see [Flask Quick Start](https://github.com/keathmilligan/flask-quickstart).

Features:
* Predictable installation and package management with [Pipenv](https://pipenv.pypa.io/en/latest/).
* PyTest unit-test support
* PyLint
* An [.editorconfig](http://editorconfig.org/) file
* Command-line argument parsing and color output support with [Click](https://click.palletsprojects.com/en/8.0.x/)

# Getting Started

The project is ready to run as is. You will need Python 3.6 or later and [Pipenv](https://pipenv.pypa.io/en/latest/).

## Installation

After cloning or downloading the repo, install the project with:

```
pipenv install
```

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
