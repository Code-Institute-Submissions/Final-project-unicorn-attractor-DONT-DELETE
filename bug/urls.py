from django.conf.urls import url
from bug.views import create_bug, preview_bug

urlpatterns = [
    url(r'create_bug/$', create_bug, name="create_bug"),
    url(r'preview_bug/(?P<id>\d+)/', preview_bug, name="preview_bug"),
]

