from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Bug


# Create your tests here.
class TestBugViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test',
                                             password='test_password')
        self.user.save()
        self.c = Client()

        self.bug = Bug.objects.create(title='test_bug',
                                      description='test_description',
                                      status="Todo",
                                      author_id=self.user.id)
        self.bug.save()
        self.c.login(username='test', password='test_password')

    def test_get_create_Bug(self):
        response = self.c.get('/bug/create_bug/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_bug.html')

    def test_preview_a_bug(self):
        response = self.c.get('/bug/preview_bug/{0}'.format(self.bug.id), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'preview_bug.html')

    def test_bug_edit(self):
        response = self.c.post('/bug/edit_bug/{0}/'.format(self.bug.id),
                               {'title': 'test_bug_changed',
                                'description': 'test_description',
                                'status': 'Doing',
                                'author_id': self.user.id
                                }
                               )
        new_updated_bug = get_object_or_404(Bug, id=1)
        self.assertEqual(new_updated_bug.title, 'test_bug_changed')
        self.assertEqual(new_updated_bug.description, 'test_description')
        self.assertEqual(new_updated_bug.status, 'Doing')

    def test_upvote_bug(self):
        response = self.c.get('/bug/upvote_bug/{0}'.format(self.bug.id), follow=True)
        bug_upvoted = get_object_or_404(Bug, id=1)
        self.assertEqual(bug_upvoted.upvotes, 1)

    def test_add_a_bug_view(self):
        response = self.c.get('/bug/add_bug/{0}'.format(self.bug.id), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_bug.html')
