FROM python:3.6.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
# We use Postgres
RUN pip install psycopg2-binary
ADD . /app/
RUN python ./manage.py migrate
RUN python ./manage.py populate_demo_data
