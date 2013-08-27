import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.template import RequestContext
from django.conf.urls.defaults import patterns
from django.shortcuts import render_to_response

class UserToCaseInline(admin.TabularInline):
    model = models.UserToCase
    extra = 0

class ImageInline(admin.TabularInline):
    model = models.ImageFile


class CaseAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'system', 'folder', 'dirTree', ]
    exclude = ('user',)
    inlines = [UserToCaseInline,
            ImageInline]

    def changelist_view(self, request, extra_context=None):
        extra_context = extracontext or {}
        extra_context['arrays'] = self.dirTree
        return super(CaseAdmin, self).changelist_view(request, extra_context=extra_context)


admin.site.register(models.Case, CaseAdmin)
admin.site.register(models.User)
admin.site.register(models.ImageFile)
