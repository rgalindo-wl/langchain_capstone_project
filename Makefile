.PHONY: api env

dependencies: 
	@echo "Installing dependencies..."
	poetry install
	poetry run pre-commit install

conf:
	cp .env.example .env

env:
	@echo "Activating virtual environment..."
	poetry shell



api:
	@echo "Running server for the API"
	poetry run uvicorn src.main:app --reload --host "localhost" --port 8000
