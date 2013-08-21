from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('editor.views',
    url(r'^$','defaultView'),
    url(r'^contact/$','defaultView'),
    )
