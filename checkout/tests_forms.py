from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from .forms import MakePaymentForm, OrderForm


class TestCartViews(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username='test',
            password='test_password')
        self.c.login(username='test',
                     password='test_password')

    def test_checkout_form_is_correct(self):
        form = MakePaymentForm(
            {
                # Visa card supplied by stripe
                'credit_card_number': '4242424242424242',
                'expiry_month': 5,
                'expiry_year': 2020,
                'cvv': 123,
                'stripe_id': 'l',  # Stripe test data
            }
        )
        self.assertTrue(form.is_valid())

    def test_checkout_form_missing_values(self):
        form = MakePaymentForm(
            {
                # Visa card supplied by stripe
                'credit_card_number': '4242424242424242',
                'expiry_month': 5,
                'expiry_year': 2020,
                'cvv': 123,
                'stripe_id': '',  # Stripe test data
            }
        )
        self.assertFalse(form.is_valid())

    def test_order_form_is_correct(self):
        form = OrderForm(
            {
                'full_name': 'test_name',
                'phone_number': '01234 567899',
                'street_address1': 'somewhere nice',
                'street_address2': 'not far away',
                'town_or_city': 'england',
                'country': 'england',
                'postcode': 'Test Data',
            }
        )
        self.assertTrue(form.is_valid())

    def test_order_form_is_missing_values(self):
        form = OrderForm(
            {
                'full_name': '',
                'phone_number': '01234 567899',
                'street_address1': 'somewhere nice',
                'street_address2': 'not far away',
                'town_or_city': 'england',
                'country': 'england',
                'postcode': 'Test Data',
            }
        )
        self.assertFalse(form.is_valid())
