from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from .models import Bug


class TestBugModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test',
                                             password='test_password')
        self.user.save()
        self.c = Client()

        self.c.login(username='test', password='test_password')

    def test_create_a_bug_model(self):
        bug = Bug.objects.create(
            title='TestBug',
            description='bug testing description',
            views=0,
            upvotes=0,
            author=self.user,
            assigned=self.user,
            status='Todo',
        )
        self.assertEqual(bug.title, 'TestBug')
        self.assertEqual(bug.description, 'bug testing description')
        self.assertEqual(bug.views, 0)
        self.assertEqual(bug.upvotes, 0)
        self.assertEqual(bug.author, self.user)
        self.assertEqual(bug.assigned, self.user)
        self.assertEqual(bug.status, 'Todo')
