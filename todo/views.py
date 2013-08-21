# Create your views here.
#from dbe.todo.models import *
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
import datetime

def index (request):
  return HttpResponse("Hello, You are at the index")

def current_datetime(request):
  now = datetime.datetime.now()
  html="<html><body>It is now %s.</body></html>" %now
  return HttpResponse(html)

@staff_member_required
def mark_done(request, pk):
    item = Item.objects.get(pk=pk)
    item.done = True
    item.save()
    return HttpResponseRedirect(reverse("admin:todo_item_changelist"))
