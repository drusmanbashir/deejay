from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover
#if not settings.LOGIN_ENABLED:
#    login_required = lambda x: x

urlpatterns = patterns('viewer.views',
        url(r'^$', 'app_root'),
        url(r'^study/(?P<study_iuid>[0-9.]+)/?$', 'study'),
        url(r'^series/(?P<series_iuid>[0-9.]+)/?$', 'series'),
        url(r'^object/(?P<instance_uid>[0-9.]+)/?$', 'instance'),
        url(r'^wado/?$', 'wado'),
        )

#if settings.LOGIN_ENABLED:
#urlpatterns += patterns('',
            #url(r'^app/?$', login_required(app_root)),
            # Below enables a simple login that will use the model authorization backend
            # Replace with your own auth system if necessary
            #url(r'^login/?$', 'django.contrib.auth.views.login'),
#    )


    # In production, these two locations must be served up statically
#if settings.DEBUG:
#    urlpatterns += patterns('django.views.static',
#            url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), 'serve', {
#                'document_root': settings.STATIC_ROOT
#                }),
#            )
