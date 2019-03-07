from django.test import TestCase
from .forms import RegisterForm


class TestUsersForms(TestCase):

    def test_register_form_has_required_input(self):
        form = RegisterForm({'username': 'test',
                             'email': 'test@hotmail.com',
                             'password1': 'testing_password',
                             'password2': 'testing_password'})
        self.assertTrue(form.is_valid())

    def test_register_form_passwords_not_matching(self):
        form = RegisterForm(
            {'username': 'test',
             'email': 'test@hotmail.com',
             'password1': 'testing_password',
             'password2': 'testing'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['password2'],
            ['The two password fields didn\'t match.'])
