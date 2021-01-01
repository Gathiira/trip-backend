FROM ubuntu:bionic
MAINTAINER Gathiira

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8

# create directory for the app user
RUN mkdir -p /opt/smokinace
WORKDIR /smokinace

RUN apt-get update -qq && apt-get install -y -qq \
    # std libs
    ca-certificates \
    wget build-essential\
    # python basic libs
    python3.6 python3.6-dev python3.6-venv gettext

RUN apt-get install -y python3-pip
COPY requirements.txt /smokinace/
RUN pip3 install -r requirements.txt
COPY . /smokinace/