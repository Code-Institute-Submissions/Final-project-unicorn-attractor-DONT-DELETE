from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


# Create your tests here.

class TestHomeViews(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username='test',
                                             password='test_password')
        self.c.login(username='test', password='test_password')

    def test_page_returns_indexpage(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_page_returns_homepage(self):
        response = self.c.get('/homepage/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_graphs_page(self):
        response = self.c.get('/statistics/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stats.html')
