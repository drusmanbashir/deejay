from knowledge.models import Answer, SBA, Mnemonic, SBAToCase
#from django import forms
from django.contrib import admin


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 2

class SBAToCaseInline(admin.TabularInline):
    model = SBAToCase
    extra = 0

class SBAAdmin(admin.ModelAdmin):
        fieldsets = (
            (None, {
                'fields': ('question', 'system', 'reference')
            }),
        )
        inlines = [
            AnswerInline,
            SBAToCaseInline,
        ]
        readonly_fields = ('created',)

admin.site.register(SBA, SBAAdmin)
admin.site.register(Answer)
admin.site.register(Mnemonic)
