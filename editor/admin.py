import models
from django.contrib import admin
from django.contrib.auth.models import User

class UserToCaseInline(admin.TabularInline):
    model = models.UserToCase
    extra = 0

class CaseAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'system', ]
    exclude = ('user',)
    inlines = [UserToCaseInline]

admin.site.register(models.Case, CaseAdmin)
admin.site.register(models.User)
