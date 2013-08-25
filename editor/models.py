from django.db import models
from django import forms
import numpy as np
from django.conf import settings


class User(models.Model):
    fn = models.CharField(max_length=10)
    sn = models.CharField(max_length=10)


class Systems(models.Model):
        HN='HN'
        CHEST='CH'
        CNS='CN'
        MSK='MS'
        PAEDS='PA'
        GI='GI'
        GU='GU'
        VAS='VA'
        BRE='BR'
        which_system=(
            (HN, 'Head & Neck'),
            (BRE, 'Breast'),
            (CHEST, 'Chest'),
            (CNS, 'Neuro'),
            (MSK, 'MSK'),
            (PAEDS, 'Paediatrics'),
            (GI, 'Gastrointestinal'),
            (GU, 'Genitourinary'),
            (VAS, 'Vascular'),
        )


class ContactForm (forms.Form):
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField()
    # sender = forms.EmailField()
    #cc_myself = forms.BooleanField(required = False)
    file = forms.FileField() 
   

def Img():
    a = np.arange(100).reshape(10, 10)
    return a


class Case(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=300, db_index=True)
    created = models.DateField(db_index=True, auto_now_add=True)
    information = models.CharField(max_length=100, db_index=True)
    system = models.CharField(max_length=2,
                            choices=Systems.which_system,
                            #default=CHEST
                              )
    folder = models.CharField(max_length=20)
    user = models.ManyToManyField(User, blank=True, null=True, through='UserToCase')

    def __unicode__(self):
        return self.title


class UserToCase(models.Model):
    case = models.ForeignKey(Case)
    user = models.ForeignKey(User)


class ImageFile (models.Model):
    imageFile = models.FileField(upload_to='uploaded_images/%Y/%m/%d')
    annotations_path = models.CharField(max_length=100)
    case = models.ForeignKey(Case)


#final = normpath(join(settings.MEDIA_ROOT,c.folder))
