FROM python:3.9-slim-buster

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY ./ /app

RUN chmod +x run.sh