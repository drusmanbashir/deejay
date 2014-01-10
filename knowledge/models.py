from django.db import models
from pacscon import models as pacscon


class SBA (models.Model):
    question = models.TextField(blank=False)
    system = models.CharField(max_length=3, choices=pacscon.System.which_system)
    case = models.ManyToManyField(pacscon.Patient, blank=True, null=True, through='SBAToCase')
    created = models.DateField(auto_now_add=True)
    reference = models.TextField(blank=True)

    def __unicode__(self):
        return self.question


class Mnemonic (models.Model):
    title = models.CharField(max_length=160, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to="/images/")

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
