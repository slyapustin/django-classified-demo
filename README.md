# Django Classified Demo website

[Django-classified](https://github.com/slyapustin/django-classified) demo project with user authorization via Facebook or Email.

## Deploy to DigitalOcean

Click the button below to deploy the Django Classified Demo app to DigitalOcean:

[![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/slyapustin/django-classified-demo/tree/do-deployment&refcode=08ce1ee690de)

## Customization

- Note: `python ./manage.py setup_project` command will load initial data to populate app Sections, Groups and Areas based on [craigslist.org](http://craigslist.org) website structure.

## Run locally

Create `.env ` file with your local settings (use `.env.example` as an example).

- Create Virtual Environment and install requirements via `pip install -r requirements.txt`.
- Create initial database schema `python ./manage.py migrate`
- Collect static files `python ./manage.py collectstatic`
- Start local development server `python ./manage.py runserver`
- Visit http://127.0.0.1:8000/
