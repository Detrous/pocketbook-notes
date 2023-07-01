SHELL := /bin/bash -o pipefail -o errexit


style:
	pre-commit run isort --all-files || true
	pre-commit run black --all-files || true

lint-flake8:
	pre-commit run flake8 --all-files

lint-bandit:
	pre-commit run bandit --all-files

lint: lint-flake8 lint-bandit

run:
	cd backend && ./run.sh