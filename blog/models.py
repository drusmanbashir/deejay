from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from markdown import markdown
from bs4  import BeautifulSoup
from django.core.files import File
from string import join
import os
from PIL import Image as PImage
from os.path import join as pjoin
from tempfile import *


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=40, db_index=True)

    class Meta:
      verbose_name_plural = "Categories"

    def __unicode__(self):
      return self.title
    
    def get_absolute_url(self):
      return "/categories/%s/" % self.slug


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=40, unique=True)
    body = models.TextField()
    body_highlighted = models.TextField(editable=False, blank = True)
    created = models.DateField(db_index=True, auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True, null=True, through='CategoryToPost')

    def images(self):
        lst = [x.image.name for x in self.image_set.all()]
        lst = ["<a href='/media/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
        return join(lst, ', ')
    images.allow_tags = True
    class Meta:
      get_latest_by = "created"

    author = models.ForeignKey(User)
    def __unicode__(self):
      return self.title

    def get_absolute_url(self):
      return "/blog/%s/%s/%s" % (self.created.year,self.created.month,self.slug)

    def save(self):
      self.body_highlighted = self.highlight_code(self.body)
      super(Post,self).save()


    def highlight_code (self, html):
      soup = BeautifulSoup(html)
      preblocks = soup.findAll('pre')
      for pre in preblocks:
        if pre.has_key('class'):
                try:
                    code = ''.join([unicode(item) for item in pre.contents])
                    code = self.unescape_html(code)
                    lexer = lexers.get_lexer_by_name(pre['class'])
                    formatter = formatters.HtmlFormatter()
                    code_hl = highlight(code, lexer, formatter)
                    pre.replaceWith(BeautifulSoup(code_hl))
                except:
                    pass
      return unicode(soup)

def unescape_html(self, html):
      html = html.replace('&lt;', '<')
      html = html.replace('&gt;', '>')
      html = html.replace('&amp;', '&')
      return html

class CategoryToPost(models.Model):
    post = models.ForeignKey(Post)
    category = models.ForeignKey(Category)

class Tag (models.Model):
  tag = models.CharField(max_length=60)
  def __unicode__(self):
    return self.tag

class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.FileField(upload_to="images/")
    caption=models.TextField(null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    posts = models.ManyToManyField(Post, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.image.name
   
    thumbnail2 = models.ImageField(upload_to="images/", blank=True, null=True)



    def size(self):
        """Image size."""
        return "%s x %s" % (self.width, self.height)
    def __unicode__(self):
        return self.image.name

    def tags_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return str(join(lst, ', '))

    def posts_(self):
        lst = [x[1] for x in self.posts.values_list()]
        return str(join(lst, ', '))

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
                                                                    (self.image.name, self.image.name))
    thumbnail.allow_tags = True
