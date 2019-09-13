FROM python:3

RUN pip3 install ddt
COPY . .

ENTRYPOINT python -m unittest