FROM        python:3.8.5-alpine3.12
COPY        . .
RUN         apk add curl \
            curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
            poetry install
