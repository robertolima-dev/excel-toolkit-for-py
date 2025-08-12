.PHONY: help install install-dev test test-cov lint format clean build publish

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install the package in development mode
	pip install -e .

install-dev:  ## Install development dependencies
	pip install -r requirements-dev.txt
	pip install -e .

test:  ## Run tests
	python -m pytest tests/ -v

test-cov:  ## Run tests with coverage
	python -m pytest tests/ -v --cov=excel_toolkit_for_py --cov-report=term-missing --cov-report=html

lint:  ## Run linting checks
	flake8 excel_toolkit_for_py/ tests/
	mypy excel_toolkit_for_py/

format:  ## Format code with black
	black excel_toolkit_for_py/ tests/

format-check:  ## Check if code is formatted correctly
	black --check excel_toolkit_for_py/ tests/

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

build:  ## Build the package
	python -m build

publish:  ## Publish to PyPI (requires authentication)
	python -m twine upload dist/*

pre-commit:  ## Install pre-commit hooks
	pre-commit install

pre-commit-run:  ## Run pre-commit on all files
	pre-commit run --all-files
