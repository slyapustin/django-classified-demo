from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy


class AuthTestCase(TestCase):
    def setUp(self):
        self.username = 'john@example.com'
        self.email = 'john@example.com'
        self.password = 'qweqweqwe'

    def create_user(self):
        User.objects.create_user(username=self.username, email=self.email, password=self.password)

    def test_email_login_page(self):
        self.create_user()
        login_page = reverse_lazy('login')
        response = self.client.post(login_page, {'email': self.email, 'password': self.password}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context, dict())
        self.assertTrue(response.context['user'].is_authenticated)
