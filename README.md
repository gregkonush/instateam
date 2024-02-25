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

Install [pipenv](https://pipenv.pypa.io/en/latest/) for managing virtual environments:

```shell
pip install pipenv
```

Create a virtual environment with Pipfile:

```shell
pipenv install
```

Start docker compose containers for development:

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
pipenv run tailwind
```

Build production minified css:

```shell
pipenv run manage.py tailwind build
```
