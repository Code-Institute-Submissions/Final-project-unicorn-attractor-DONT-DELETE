from django.conf.urls import url
from bug.views import create_bug, preview_bug, delete_bug, edit_bug, add_bug, upvote_bug

urlpatterns = [
    url(r'create_bug/$',create_bug, name="create_bug"),
    url(r'edit_bug/(?P<id>\d+)/', edit_bug, name="edit_bug"),
    url(r'upvote_bug/(?P<id>\d+)/', upvote_bug, name="upvote_bug"),
    url(r'add_bug/(?P<id>\d+)/', add_bug, name="add_bug"),
    url(r'preview_bug/(?P<id>\d+)/', preview_bug, name="preview_bug"),
    url(r'delete_bug/(?P<id>\d+)/', delete_bug, name="delete_bug"),
]

