"""unicornApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from home.views import index, home
from users import urls as users_urls
from bug import urls as bug_urls
from feature import urls as feature_urls
from home import urls as home_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include(home_urls)),
    url(r'users/', include(users_urls)),
    url(r'bug/', include(bug_urls)),
    url(r'feature/', include(feature_urls)),
    url(r'cart/', include(cart_urls)),
    url(r'checkout/', include(checkout_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
