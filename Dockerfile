FROM python:3.8

# set environment variables
ENV PYTHONUNBUFFERED 1

WORKDIR /smokinace

COPY requirements.txt /smokinace/
RUN pip3 install -r requirements.txt
COPY . /smokinace/