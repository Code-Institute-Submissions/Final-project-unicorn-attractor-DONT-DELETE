from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from .models import Feature
from django.utils import timezone
from django.shortcuts import get_object_or_404
from . import urls
from . import views

# Create your tests here.
class TestFeatureViews(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='test', 
                                        password='test_password')

        self.user.save()

        self.c = Client()

        self.feature = Feature.objects.create(title ='test_feature', 
                                              description = 'test_description',
                                              price = 111,
                                              author_id = self.user.id)

        self.feature.save()
        self.c.login(username='test', password='test_password')

    def test_get_create_feature_form(self):
        response = self.c.get('/feature/create_feature/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_feature.html')

    def test_preview_a_feature(self):
        response = self.c.get('/feature/preview_feature/{0}'.format(self.feature.id), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'preview_feature.html')

    def test_feature_edit(self):
        response = self.c.post('/feature/edit_feature/{0}/'.format(self.feature.id),
                                {'title': 'test_feature_changed',
                                'description': 'test_description',
                                'price': 222,
                                'author_id': self.user.id
                                }
                            )
        new_updated_feature = get_object_or_404(Feature, id=1)
        self.assertEqual(new_updated_feature.title, 'test_feature_changed')
        self.assertEqual(new_updated_feature.description, 'test_description')
        self.assertEqual(new_updated_feature.price, 222)
    
    def test_upvote_feature(self):
        self.c.login(username='test', password='test_password')
        response = self.c.get('/feature/upvote_feature/{0}'.format(self.feature.id), follow=True)
        feature_upvoted = get_object_or_404(Feature, id=1)
        self.assertEqual(feature_upvoted.upvotes, 1)

