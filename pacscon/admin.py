from pacscon import models as pacs_models
from django.contrib import admin
from django.db.models.base import ModelBase

for name, var in pacs_models.__dict__.items():
        if type(var) is ModelBase:
                admin.site.register(var)
