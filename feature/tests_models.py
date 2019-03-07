from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from .models import Feature


class TestFeatureModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            password='test_password')
        self.user.save()
        self.c = Client()

        self.c.login(username='test',
                     password='test_password')

    def test_create_a_bug_model(self):
        feature = Feature.objects.create(
            title='Test Feature',
            description='feature testing description',
            views=0,
            upvotes=0,
            author=self.user,
            purchased=0,
            price=1200,
        )
        self.assertEqual(feature.title,
                         'Test Feature')
        self.assertEqual(feature.description,
                         'feature testing description')
        self.assertEqual(feature.views, 0)
        self.assertEqual(feature.upvotes, 0)
        self.assertEqual(feature.author, self.user)
        self.assertEqual(feature.purchased, 0)
        self.assertEqual(feature.price, 1200)
