from django.conf.urls import url
from home.views import index, home

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^homepage/', home, name="home"),
]
