# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Systems(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    class Meta:
        db_table = 'systems'

    def __unicode__(self):
        return self.name

class Teaching(models.Model):
    case_id = models.BigIntegerField(primary_key=True)
    date_added = models.DateField(null=True, blank=True)
    system_name = models.ForeignKey(Systems, null=True, db_column='system_name', blank=True)

    class Meta:
        db_table = 'teaching'

    def __unicode__(self):
        return u"%s" % self.case_id
