from django.test import TestCase
from .forms import New_posts, Bug_status, Comment_form

# Create your tests here.

class TestBugForm(TestCase):
    def test_bug_has_name_and_description(self):
        form = New_posts({'title': 'bugtest', 'description': 'bugs description for test'})
        self.assertTrue(form.is_valid())

    def test_bug_missing_name_or_description(self):
        form = New_posts({'description': 'bugs description for test'})
        self.assertFalse(form.is_valid())