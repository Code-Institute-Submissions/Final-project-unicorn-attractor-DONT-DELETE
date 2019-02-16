from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.http import HttpRequest
from . import views
from .models import Bug


# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.User.objects.create_user(username = 'test',
                                password = 'testing123',
                                email = 'test@something.co.uk')

        self.Bug.objects.create(title='test_bug',
                            description='testing description',
                            status='Todo',
                            author_id = 1)

                   
        

