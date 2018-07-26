FROM python:3.6.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -U pip
RUN pip install -r requirements.txt

RUN pip install psycopg2-binary
RUN pip install gunicorn

ADD . /app/

RUN python ./manage.py collectstatic --noinput
