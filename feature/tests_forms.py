from django.test import TestCase
from .forms import New_posts, Comment_form


class TestFeatureForm(TestCase):
    def test_feature_has_name_description_price(self):
        form = New_posts(
            {'title': 'feature_test',
             'description': 'features description for test',
             'price': 111})
        self.assertTrue(form.is_valid())

    def test_feature_missing_name_or_description_or_price(self):
        form = New_posts({'title': 'feature_test',
                          'description': '',
                          'price': 111})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['description'], ['This field is required.'])


class TestfeatureCommentForm(TestCase):
    def test_bug_comment_form(self):
        form = Comment_form({'comment': 'testing comments form'})
        self.assertTrue(form.is_valid())
