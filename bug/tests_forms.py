from django.test import TestCase
from .forms import New_posts, Comment_form


class TestBugForm(TestCase):
    def test_bug_has_name_description_status(self):
        form = New_posts({'title': 'bugtest',
                          'description': 'description test',
                          'status': 'Todo'})
        self.assertTrue(form.is_valid())

    def test_bug_missing_name_or_description(self):
        form = New_posts({'description': 'bugs description for test'})
        self.assertFalse(form.is_valid())


class TestBugCommentForm(TestCase):
    def test_bug_comment_form(self):
        form = Comment_form({'comment': 'testing comments form'})
        self.assertTrue(form.is_valid())
