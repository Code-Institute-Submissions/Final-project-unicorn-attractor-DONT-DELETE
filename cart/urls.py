from django.conf.urls import url
from cart.views import view_cart, add_to_cart, delete_cart

urlpatterns = [
    url(r'^view_cart/', view_cart, name='view_cart'),
    url(r'^add_to_cart/(?P<id>\d+)/', add_to_cart, name='add_to_cart'),
    url(r'^delete_cart/(?P<id>\d+)/', delete_cart, name='delete_cart'),
]
