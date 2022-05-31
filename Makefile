.PHONY: install virtualenv ipython clean pflake8


install:
	@echo "Install for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'


virtualenv:
	@.venv/bin/python -m pip -m venv .venv 


ipython:
	@.venv/bin/python

lint:
	@.venv/bin/pflake8

fmt:
	@.venv/bin/isort dundie tests integration
	@.venv/bin/black dundie tests integration
	
test:
	@.venv/bin/pytest -s --forked

watch:
	@ls **/*.py | entr pytest --forked

clean: ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

docs:
	@mkdocs build --clean 

docs-serve:
	@mkdocs serve

build:
	@python setup.py sdist bdist_wheel


publish-test:
	@twine upload --repository testpypi dist/*

publish:
	@twine upload dist/*
