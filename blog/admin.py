import models
from django.contrib import admin
#from django.contrib.auth.models import User
#from django_markdown.admin import MarkdownModelAdmin

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryToPostInline(admin.TabularInline):
    model = models.CategoryToPost
    extra = 2

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)
    inlines = [CategoryToPostInline]
    list_display=["title","images"]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

class ImageAdmin (admin.ModelAdmin):
  search_fields=["title"]
  list_display = ["__unicode__","title","size","tags_","posts_","thumbnail","created"]
  list_filter=["tags","posts"]

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Image,ImageAdmin)
