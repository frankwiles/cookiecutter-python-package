# Cookiecutter to make a Python Package

A simple Python 3.7+ starter template using [cookiecutter](https://github.com/audreyr/cookiecutter).

**NOTE**: At this point I do not intend to actively support this cookiecutter
for general/public consumption.  That may change, but for now this is just for
my own personal use cases.  It is however BSD licensed, so you can do whatever
you want with it.

Basically, reach out before putting a bunch of work into a pull request as it
may or may not be something I'm interested in incorporating.

## Usage

```shell
$ cookiecutter https://github.com/frankwiles/cookiecutter-python-package
```

## Decisions

This cookiecutter is a bit opinionated, in short it will use:

- Python 3.7+
- pytest
- Click if it's a command line utility
- Django if it's web based

## Project Information

- [License](LICENSE.txt)
- [Authors](AUTHORS.md)
- [Changelog](CHANGELOG.md)
