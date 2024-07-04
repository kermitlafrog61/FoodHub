FROM python:3.10-slim

# Declaring ENV Variables
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \    
    # Poetry's configuration:
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.3

# Setting workdir
WORKDIR /app

# Downloading poetry and installing dependencies
RUN pip install poetry==${POETRY_VERSION}

COPY src/poetry.lock src/pyproject.toml /app/
RUN poetry install --no-ansi

# Adding all neccesary scripts to be runable
COPY docker/scripts/ /usr/local/bin
RUN chmod +x /usr/local/bin/*
ENV PATH="/usr/local/bin:${PATH}"

# Adding other additional parts to image
COPY src/ .
