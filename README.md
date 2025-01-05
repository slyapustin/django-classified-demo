# Django Classified Demo website

[Django-classified](https://github.com/slyapustin/django-classified) demo project with user authorization via Facebook or Email.

## Demo web site

You can check demo project running here: [django-classified.herokuapp.com](https://django-classified.herokuapp.com?utm_source=github).

## Deploy to Heroku (this is free)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Customization

- Note: `python ./manage.py setup_project` command will load initial data to populate app Sections, Groups and Areas based on [craigslist.org](http://craigslist.org) website structure.

## Run locally

Create `.env ` file with your local settings (use `.env.example` as an example).

- Create Virtual Environment and install requirements via `pip install -r requirements.txt`.
- Create initial database schema `python ./manage.py migrate`
- Collect static files `python ./manage.py collectstatic`
- Start local development server `python ./manage.py runserver`
- Visit http://127.0.0.1:8000/
