import models
from django.contrib import admin
from django.contrib.auth.models import User

class UserToCaseInline(admin.TabularInline):
    model = models.UserToCase
    extra = 0

class ImageInline(admin.TabularInline):
    model = models.ImageFile


class CaseAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'system', 'folder', ]
    exclude = ('user',)
    inlines = [UserToCaseInline,
            ImageInline]

admin.site.register(models.Case, CaseAdmin)
admin.site.register(models.User)
admin.site.register(models.ImageFile)
