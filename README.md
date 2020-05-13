# Django Classified Demo website #

[Django-classified](https://github.com/inoks/django-classified) demo project with user authorization via social network accounts or e-mail.

## Demo web site
You can check demo project running here: [django-classified.herokuapp.com](https://django-classified.herokuapp.com?utm_source=github).

## Deploy to Heroku (this is free)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Customization
- Note: `python ./manage.py setup_project` command will load initial data to populate app Sections, Groups and Areas based on [craigslist.org](http://craigslist.org) website structure.

## Run locally
Create `.env ` file with your local settings (use `.env.example` as an example).
- Create Virtual Environment  and install requirements via `pip install -r requirements.txt`.
- Create initial database schema `python ./manage.py migrate`
- Start local development server `python ./manage.py runserver`
- Visit http://127.0.0.1:8000/

## Development notes
This demo is a work in progress and is intended to help you get started with django-classified.

This demo project incorporates django-allauth, and is based upon the allauthdemo of Gajesh Bhat (https://dev.to/gajesh/the-complete-django-allauth-guide-la3 https://github.com/gajeshbhat/django-experiments/tree/master/allauthdemo). However, the files for this demo have been extensively modified to better integrate with django-classified.

There are a couple of issues within the demo that could be handled better. The first of these is that when an authentication e-mail is sent, after initial set-up of an account, there is no obvious way to re-send that e-mail if it does not arrive. On the "authentication message sent" page there is a message to the user as to how to complete this, but it would be better if there were some other more direct method.

The indirect method is to get the user to go to the log-in page and log-in with their user name and password - this will trigger another authentication e-mail, if they have not already authenticated.

This is a django-allauth "feature", which the developers seem not to consider a bug or obvious missing feature.

The other issue is that when using OpenID to log-in the user has to either type in their choice of OpenID server, or click one the the links below. It would be more elegant to have a pop-up/select menu.

OpenID appears not to require an application to be set-up for authorisation, whereas the other social network methods do.

The social network settings in the settings.py file are examples, and may or may not be functional in all cases.

In general there are several areas where it would be preferable, from a user interface perspective, for the user to be warned of form completion errors as they are completing the form. However, some form elements will not show an error until after the form has been executed and returned by the server.

There are lots of notes in the settings.py file.