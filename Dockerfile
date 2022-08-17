FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

# install global dependencies
RUN apt-get update --fix-missing
RUN apt install docker.io -y
RUN apt-get install -y git
RUN apt-get install -y python3 python3-dev python3-setuptools
RUN apt-get install -y python3-pip virtualenv


# expose ports
EXPOSE 5000

# create a virtual environment and install local dependencies
RUN virtualenv --python=/usr/bin/python3 /opt/env
ADD ./requirements.txt /opt/venv/requirements.txt
RUN pip3 install -r /opt/venv/requirements.txt


# add source
ADD src /opt/src

# start supervisor
CMD python3 /opt/src/app.py

