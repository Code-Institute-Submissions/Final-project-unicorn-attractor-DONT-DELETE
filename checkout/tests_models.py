from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class TestCartViews(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username='test',
                                             password='test_password')
        self.c.login(username='test', password='test_password')

        def test_create_a_order_model(self):
            order = objects.create(
                {
                    'full_name': 'test_name',
                    'phone_number': '01234 567899',
                    'street_address1': 'somewhere nice',
                    'street_address2': 'not far away',
                    'town_or_city': 'england',
                    'country': 'england',
                    'postcode': 'Test Data',
                    'date': '2018-02-02'
                }
            )

        self.assertEqual(order.full_name, 'Test_name')
        self.assertEqual(order.phone_number, '01234 567899')
        self.assertEqual(order.street_address1, 'somewhere nice')
        self.assertEqual(order.street_address2, 'not far away')
        self.assertEqual(order.town_or_city, 'england')
        self.assertEqual(order.country, 'england')
        self.assertEqual(order.postcode, 'Test Data')
        self.assertEqual(order.date, '2018-02-02')
