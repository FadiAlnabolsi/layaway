"""layaway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # user auths urls
    url(r'^accounts/login/$', 'layaway.views.login'),
    url(r'^accounts/auth/$', 'layaway.views.auth_view'),
    url(r'^accounts/logout/$', 'layaway.views.logout'),
    url(r'^accounts/loggedin/$', 'layaway.views.loggedin'),
    url(r'^accounts/invalid/$', 'layaway.views.invalid_login'),
    url(r'^accounts/register/$', 'layaway.views.register_user'),
    url(r'^accounts/register_success/$', 'layaway.views.register_success'),

    url(r'', include('layawayapp.urls')),
]
