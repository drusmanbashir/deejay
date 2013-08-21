
from django import template
register = template.Library()

def lower(value):
    return value.lower()
  
register.filter('lower',lower)
