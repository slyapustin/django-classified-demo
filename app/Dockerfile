FROM python:3.7.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements/default.txt /app/
ADD requirements/docker.txt /app/

RUN pip install -U pip
RUN pip install -r docker.txt

ADD . /app/
