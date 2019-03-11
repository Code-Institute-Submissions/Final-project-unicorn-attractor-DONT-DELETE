from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from feature.models import Feature


class TestCartViews(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username='test',
                                             password='test_password')
        self.c.login(username='test', password='test_password')

        self.feature = Feature.objects.create(
            title='Test Feature',
            description='feature testing description',
            views=1,
            upvotes=1,
            author=self.user,
            purchased=1,
            price=1200,
        )
        self.feature.save()

    def test_page_returns_index_page(self):
        response = self.c.get('/cart/view_cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_cart_items_are_added(self):
        response = self.c.get('/cart/add_to_cart/{0}'.format(self.feature.id), follow=True)
        self.assertEqual(response.status_code, 200)
        session = self.c.session
        print(session['cart'])
        cart = session['cart']
        self.assertEqual(cart, {'1': 1})

    def test_cart_item_has_been_removed(self):
        response = self.c.get('/cart/delete_cart/{0}'.format(
            self.feature.id), follow=True)
        self.assertEqual(response.status_code, 200)
        session = self.c.session
        cart = session['cart']
        self.assertEqual(cart, {})
