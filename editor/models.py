from django.db import models
from django import forms
import numpy as np

class ContactForm (forms.Form):
 # subject = forms.CharField(max_length=100)
 # message = forms.CharField()
 # sender = forms.EmailField()
  #cc_myself = forms.BooleanField(required = False)
  file = forms.FileField()

class ImageFile (models.Model):
  imageFile = models.FileField(upload_to='uploaded_images/%Y/%m/%d')

def Img():
  a = np.arange(100).reshape(10,10)
  return a
