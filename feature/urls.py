from django.conf.urls import url
from feature.views import create_feature

urlpatterns = [
    url(r'create_feature/$', create_feature, name="create_feature"),
]

