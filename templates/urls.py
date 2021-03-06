from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deejay.views.home', name='home'),
    # url(r'^deejay/', include('deejay.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#r tells django that string is raw and no escapes
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/',include('blog.urls')),
    url(r'^todo/', include ('todo.urls')),
    url(r'^markdown/',include('django_markdown.urls')),
    
)
