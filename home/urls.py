from django.conf.urls import url
from home.views import index, home, statistics, data_for_graphs

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^homepage/', home, name="home"),
    url(r'^statistics/', statistics, name="statistics"),
    url(r'^ajax/data', data_for_graphs, name="data_for_graphs"),
]
