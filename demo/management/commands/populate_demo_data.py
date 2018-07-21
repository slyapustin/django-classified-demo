from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create Demo Classified Admin'

    def create_admin(self):
        username = 'admin'
        password = 'admin'

        User.objects.create_user(
            username=username,
            password=password,
            is_superuser=True,
            is_staff=True
        )

        self.stdout.write(
            'Super user was created successfully. '
            'Please use username: {} and password: {} to access /admin/'.format(
                username,
                password
            ))

    def handle(self, *args, **options):
        self.create_admin()
