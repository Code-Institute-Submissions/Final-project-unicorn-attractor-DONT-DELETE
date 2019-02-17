from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from . import views
from . import urls



class TestCartViews(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username='test',
                                             password='test_password')
        self.c.login(username='test', password='test_password')


    def test_checkout_page(self):
        response = self.c.get('/checkout/checkout/')
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')