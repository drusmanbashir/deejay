from django.db import models
from pacscon import models as pacscon

class MCC (models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __unicode__(self):
        return self.question

class Tag (models.Model):
    tag = models.CharField(max_length=20)

    def __unicode__(self):
        return self.tag

class SBA (models.Model):
   # title = models.CharField(max_length=160, null=False)
    question = models.TextField(blank=False)
    system = models.CharField(max_length=3, choices=pacscon.System.which_system)
    case = models.ManyToManyField(pacscon.Patient, blank=True, null=True, through='SBAToCase')
    tag = models.ManyToManyField(Tag, through='SBAToTag')
    created = models.DateField(auto_now_add=True)
    reference = models.TextField(blank=True)
    explanation = models.TextField(blank=True)

    def __unicode__(self):
        return self.question


class Factoid (models.Model):
    fact = models.TextField(blank=False)
    system = models.CharField(max_length=3, choices=pacscon.System.which_system)
    created = models.DateField(auto_now_add=True)
    reference = models.TextField(blank=True)
    tag = models.ManyToManyField(Tag, through='FactoidToTag')

    def __unicode__(self):
        return self.fact


class Mnemonic (models.Model):
    title = models.CharField(max_length=160, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to="/images/", null=True, blank=True)

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    #id = models.AutoField(primary_key=True)
    body = models.TextField()
    correct = models.BooleanField(default=False)
    sba = models.ForeignKey(SBA, null=True)

    def __unicode__(self):
        return self.body

class SBAToCase(models.Model):
    sba = models.ForeignKey(SBA)
    case = models.ForeignKey(pacscon.Patient)

class FactoidToTag(models.Model):
    factoid = models.ForeignKey(Factoid)
    tag = models.ForeignKey(Tag)

class SBAToTag(models.Model):
    sba = models.ForeignKey(SBA)
    tag = models.ForeignKey(Tag)
