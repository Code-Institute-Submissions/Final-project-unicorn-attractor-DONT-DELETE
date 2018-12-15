from django.urls import path
from posts.views import index, create_post

urlpatterns = [
    path('', index, name="index"),
    path('create_post/', create_post, name="create_post"),
]