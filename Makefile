current-dir := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SHELL = /bin/sh
start: install-deps
install-deps:
	@if [ -z $(shell which pipenv) ]; then echo "ERROR: missing software required (pip install pipenv)" > /dev/stderr && exit 1; fi
	@PIPENV_VENV_IN_PROJECT=1 pipenv install --dev
install:
	@PIPENV_VENV_IN_PROJECT=1 pipenv install $(dep)==$(ver)
install-dev:
	@PIPENV_VENV_IN_PROJECT=1 pipenv install $(dep)==$(ver) --dev
uninstall:
	@pipenv uninstall $(dep)
run:
	@bash -c "pipenv run app" 
run-tests:
	@bash -c "pipenv run test" 
format: 
	@pipenv run isort
	@pipenv run black
check-format:
	@pipenv run check-isort
	@pipenv run check-black
	@pipenv run check-flake8
check-types:
	@pipenv run check-types
.PHONY: start install-deps install install-dev uninstall build deploy run run-tests format check-format check-types
