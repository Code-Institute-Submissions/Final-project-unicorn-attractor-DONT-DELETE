from django.conf.urls import url
from cart.views import view_cart

urlpatterns = [
    url(r'^view_cart/', view_cart, name='view_cart'),
]
