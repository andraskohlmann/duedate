FROM python:3

COPY . .

ENTRYPOINT python -m unittest