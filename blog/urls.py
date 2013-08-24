from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from blog.models import Category, Post

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # Home page
    url(r'^$','getLatestPost', name='latest'),
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
      model=Post,
      paginate_by=5,
      )),

    # Blog posts
    url(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)$', 'getPost',name='single'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$','getList',name='list'),
    url(r'^all/?$','getList',name='getAll'),
    #url(r'^all$','getList',name='all'),
    #  url(r'^categories/(?P<categorySlug>\w+)/?$', 'blog.views.getCategory',),
    # url(r'^categories/(?P<categorySlug>\w+)/(?P<selected_page>\d+)/?$', 'blog.views.getCategory'),


    # RSS feeds
    #url(r'^feeds/posts/$', PostsFeed()),
    

    )
