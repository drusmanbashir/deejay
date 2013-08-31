import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.template import RequestContext
from django.conf.urls.defaults import patterns
from django.shortcuts import render_to_response
from django.conf import settings

class UserToCaseInline(admin.TabularInline):
    model = models.UserToCase
    extra = 0

class ImageInline(admin.TabularInline):
    model = models.ImageFile


class CaseAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'system', 'folder', 'dirTree', ]
    exclude = ('user',)
    inlines = [UserToCaseInline,
           # ImageInline
    ]

    class Media:
        js = (
            #MEDIA_URL + 'js/jquery.js',
            settings.MEDIA_URL + 'js/editor_admin.js',


        )


admin.site.register(models.Case, CaseAdmin)
admin.site.register(models.User)
admin.site.register(models.ImageFile)
