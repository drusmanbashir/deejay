from django.contrib import admin
import models

class TrialAdmin(admin.ModelAdmin):
        fields = ['case_id', 'system_name']

admin.site.register(models.Teaching, TrialAdmin)
admin.site.register(models.Systems)
