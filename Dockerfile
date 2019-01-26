FROM python:3.6
ENV LANG C.UTF-8

RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install dnsutils -y
