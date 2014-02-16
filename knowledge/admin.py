from knowledge.models import Answer, SBA, Mnemonic, SBAToCase, SBAToTag, Factoid, Tag, FactoidToTag, MCC
#from django import forms
from django.contrib import admin


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0
class TagInline(admin.StackedInline):
    model = SBAToTag
    extra = 0

class FactoidTagInline(admin.StackedInline):
    model = FactoidToTag
    extra = 0
class SBAToCaseInline(admin.TabularInline):
    model = SBAToCase
    extra = 0

class FactoidAdmin(admin.ModelAdmin):
    inlines = [
            FactoidTagInline,
            ]


class SBAAdmin(admin.ModelAdmin):
        fieldsets = (
            (None, {
                'fields': ('question', 'system', 'explanation', 'reference')
            }),
        )
        inlines = [
            TagInline,
            SBAToCaseInline,
            AnswerInline,
        ]
        readonly_fields = ('created',)

admin.site.register(SBA, SBAAdmin)
#admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Factoid, FactoidAdmin)
admin.site.register(Mnemonic)
admin.site.register(MCC)
