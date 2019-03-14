from django.conf.urls import url, include
from .views import register, profile, logout
from users import url_reset
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'register/', register, name="register"),
    url(r'profile/', profile, name="profile"),
    url(r'login/', auth_views.LoginView.as_view(
        template_name="login.html"), name="login"),
    url(r'logout/', logout, name="logout"),
    url(r'^password_reset/', include(url_reset)),
]
