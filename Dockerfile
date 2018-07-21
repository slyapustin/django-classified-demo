FROM python:3.6.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
RUN python3 ./manage.py migrate
RUN python3 ./manage.py populate_demo_data

CMD python3 ./manage.py runserver 0.0.0.0:8000
