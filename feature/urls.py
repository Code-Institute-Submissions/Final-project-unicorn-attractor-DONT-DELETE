from django.conf.urls import url
from feature.views import create_feature, preview_feature

urlpatterns = [
    url(r'create_feature/$', create_feature, name="create_feature"),
    url(r'preview_feature/(?P<id>\d+)/', preview_feature, name="preview_feature"),

]

