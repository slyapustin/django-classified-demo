import json

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django_classified.models import Area, Section, Group


class Command(BaseCommand):
    help = 'Create Demo Classified Admin'

    def create_admin(self):
        username = 'admin'
        password = 'admin'
        email = 'admin@example.com'

        try:
            User.objects.create_superuser(
                username=username,
                password=password,
                email=email
            )
        except IntegrityError:
            self.stdout.write('Admin user already created')
            return

        self.stdout.write(
            'Superuser {}/{} was created successfully.'.format(
                username,
                password
            ))

    def populate_craigslist_data(self):
        # Clone structure of Craigslist
        self.stdout.write('Loading Sections')
        sections = json.load(open('demo/craigslist_data/Types.json'))
        sections_dict = dict()
        for section in sections:
            obj, _ = Section.objects.get_or_create(
                title=section['Description']
            )
            # To speed up access later
            sections_dict[section['Type']] = obj

        self.stdout.write('Loading Groups')
        categories = json.load(open('demo/craigslist_data/Categories.json'))
        for category in categories:
            Group.objects.get_or_create(
                slug=category['Abbreviation'],
                defaults=dict(
                    section=sections_dict[category['Type']],
                    title=category['Description']
                )
            )

        country_code = 'GB'
        self.stdout.write('Loading Areas for %s' % country_code)
        areas = json.load(open('demo/craigslist_data/Areas.json'))
        for area in areas:
            if area.get('Country') == country_code:
                Area.objects.get_or_create(
                    slug=area.get('Abbreviation'),
                    defaults=dict(
                        title=area.get('ShortDescription')
                    )
                )

    def handle(self, *args, **options):
        self.create_admin()
        self.populate_craigslist_data()
