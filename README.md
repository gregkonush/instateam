# Instateam

## Installation instructions

Install python with [pyenv](https://github.com/pyenv/pyenv):

```shell
brew install pyenv
```

Install python 3.12.2:

```shell
pyenv install 3.12.2
# set as global version
pyenv global 3.12.2
```

Install django:

```shell
pip install django
```

Install [pipx](https://github.com/pypa/pipx) for isolated python apps
Install [poetry](https://python-poetry.org/docs/#installation) for managing virtual environments:

```shell
pipx install poetry
```

Create a virtual environment with poetry:

```shell
poetry shell
```

Start docker compose db container for development:

```shell
docker compose up -d
```

Build docker image:

```shell
docker compose build
```

Install pre-commit hook:

```shell
pre-commit install
```

To run tailwindcss styling server:

```shell
poetry run python manage.py tailwind start
```

Build production minified css:

```shell
poetry run python manage.py tailwind build
```
