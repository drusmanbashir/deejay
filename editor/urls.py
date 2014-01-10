from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('editor.views',
    url(r'^$', 'defaultView'),
    url(r'^contact/$', 'defaultView'),
)
