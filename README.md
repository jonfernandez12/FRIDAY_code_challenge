# FRIDAY_code_challenge
Code challenge for FRIDAY, German branch of FRIDAY Insurance S.A.

To access project documentation go to https://jonfernandez12.github.io/FRIDAY_code_challenge/public/index.html

Jon Fernández Bedia

## Requisites

- [pipenv](https://pypi.org/project/pipenv/)
- If you are using Visual Studio Code, you need to install [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
## Start

```
make start
```

### Git Hooks

* **Pre-commit**: before each commit the `make run-tests` command will be executed. 

Note: If you want to ignore the pre-commit hook, add the flag `--no-verify` to the commit command.


## Install dependencies

```
make install-deps
```

## Add/remove dependency

```
# Install dependency
make install dep={{dependency}} ver={{dependency_version}} # Example: make install dep=requests ver=2.26.0
make install-dev dep={{dependency}} ver={{dependency_version}} # Example: make install-dev dep=requests ver=2.26.0

# Uninstall dependency
make uninstall dep={{dependency}} # Example: make uninstall dep=requests
```

## Run

Runs main application, located in app/main.py.

```
make run
```

## Run tests

Run all tests defined in app/services/tests/test.py.

```
make run-tests
```

## Format code

Orders dependencies with Isort and formats the code using Black.

```
make format
```

## Check format

Checks code format based on Isort, Black and Flake8 requirements.

```
make check-format
```

## Check types

Checks if all types are well typed.

```
make check-types
```

## Generate docs

Generate all documentation in HTML format and leaves it in public/index.html, open with your favorite browser.

```
make docs
```
