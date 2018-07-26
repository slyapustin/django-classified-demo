# Django Classified Demo website #

[Django-classified](https://github.com/inoks/django-classified) demo project with user authorization via Facebook or Email.

## Demo web site

You can check demo project running here: http://classified.pzbz.ru

## Running on local machine

- `git clone git@github.com:inoks/django-classified-demo.git`
- `cd django-classified-demo/app/`
- `python3 -m venv .`
- `source bin/activate`
- `pip install -r requirements/default.txt`
- `python3 ./manage.py migrate`
- `python3 ./manage.py populate_demo_data`
- `python3 ./manage.py runserver`
- Open http://localhost:8000/ in your browser

## Running with Docker

- Install [Docker](https://www.docker.com/community-edition)
- `git clone git@github.com:inoks/django-classified-demo.git`
- `cd django-classified-demo/`
- `docker-compose up -d`
- `docker-compose run web python ./manage.py populate_demo_data`
- Open http://localhost:8000/ in your browser

## Customisation

 - Note: `populate_demo_data` management command will load initial data to populate app
    Sections, Groups and Areas based on [craigslist.org](http://craigslist.org) website structure.

 - Use username `admin` and `password` admin to access [Django Classified Admin](http://localhost:8000/admin/).
