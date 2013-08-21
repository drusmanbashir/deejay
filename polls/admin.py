from polls.models import Poll
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
  fields=['question','pub_date']

admin.site.register(Poll,PollAdmin)
