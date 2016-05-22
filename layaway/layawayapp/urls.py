from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import patterns

urlpatterns = [
    url(r'^$', 'layawayapp.views.homepage'),
    url(r'^about_us$', 'layawayapp.views.about_us'),
    url(r'^my_account$', 'layawayapp.views.my_account'),
    url(r'^events$', 'layawayapp.views.my_account'),
    url(r'^events/(?P<id>[0-9]+)', 'layawayapp.views.event_instance')
]
