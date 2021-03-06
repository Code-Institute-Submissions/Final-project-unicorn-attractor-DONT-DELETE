from django.conf.urls import url
from feature.views import create_feature, \
    preview_feature, delete_feature, \
    edit_feature, upvote_feature, \
    brought_feature

urlpatterns = [
    url(r'create_feature/$', create_feature,
        name="create_feature"),
    url(r'preview_feature/(?P<id>\d+)/', preview_feature,
        name="preview_feature"),
    url(r'brought_feature/(?P<id>\d+)/', brought_feature,
        name="brought_feature"),
    url(r'delete_feature/(?P<id>\d+)/', delete_feature,
        name="delete_feature"),
    url(r'edit_feature/(?P<id>\d+)/', edit_feature,
        name="edit_feature"),
    url(r'upvote_feature/(?P<id>\d+)/', upvote_feature,
        name="upvote_feature"),

]
