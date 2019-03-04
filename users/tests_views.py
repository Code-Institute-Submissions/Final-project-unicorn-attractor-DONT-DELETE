from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class TestUserViews(TestCase):
    def setUp(self):
        self.c = Client()

    def test_get_user_registration_page(self):
        response = self.c.get('/users/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_get_user_login_page(self):
        response = self.c.get('/users/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_get_users_profile_page(self):
        user = User.objects.create_user(username='test', password='test_password')
        self.c.login(username='test', password='test_password')
        response = self.c.get('/users/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
