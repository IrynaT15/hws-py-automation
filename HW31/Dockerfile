FROM jenkins/jenkins:lts-jdk17

USER root

RUN apt-get update && \
    apt-get install -y python3.11 python3.11-venv python3-pip

RUN python3.11 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"


RUN pip3 install --upgrade pip setuptools && \
    pip3 install pytest
