# FRIDAY_code_challenge
Code challenge for FRIDAY enterprise

## Requisites

- [pipenv](https://pypi.org/project/pipenv/)
- If you are using Visual Studio Code, you need to install [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
## Start

```bash
make start
```

### Git Hooks

* **Pre-commit**: before each commit the `make run-tests` command will be executed. 

Note: If you want to ignore the pre-commit hook, add the flag `--no-verify` to the commit command.


## Install dependencies

```bash
make install-deps
```

## Add/remove dependency

```bash
make install dep={{dependency}} ver={{dependency_version}} # Example: make install dep=requests ver=2.26.0
make install-dev dep={{dependency}} ver={{dependency_version}} # Example: make install-dev dep=requests ver=2.26.0

make uninstall dep={{dependency}} # Example: make uninstall dep=requests
```

## Run

Runs main application, located in app/main.py .
```bash
make run
```

## Run tests

Run all tests defined in app/services/tests/test.py.
```bash
make run-tests
```

## Format code

Orders dependencies with isort and formats the code using the requirementes defined on pyproject.toml.

```bash
make format
```

## Check format

```bash
make check-format
```

## Check types
```bash
make check-types
```