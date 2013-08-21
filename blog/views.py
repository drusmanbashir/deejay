import time
from settings import MEDIA_URL
from calendar import month_name
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from django.template import RequestContext, Context, loader
from blog.models import *
from django.contrib.syndication.views import Feed
from django.contrib.flatpages.models import FlatPage
from django.http import Http404, HttpResponse

def mkmonth_lst():
  """Make a list of months to show archive links. """

  if not Post.objects.count(): return []

  year, month = time.localtime()[:2]
  first = Post.objects.order_by("created")[0]
  fyear = first.created.year
  fmonth = first.created.month
  months = []

  for y in range (year, fyear-1,-1):
    start,end = 12,0
    if y == year: start = month
    if y == fyear: end = fmonth-1

    for m in range(start,end, -1):
      months.append((y, m, month_name[m]))
  return months


def getPost(request, postSlug):
    # Get specified post
    try:
      post = Post.objects.filter(slug=postSlug)
    except Post.DoesNotExist:
      raise Http404
    
    # Display specified post
    return render_to_response("blog/single.html", dict(posts=post,images=images, user=request.user,
                                                months=mkmonth_lst(), archive=True))

def getLatestPost (request):
  try:  
    post=Post.objects.latest('created')
    images=post.image_set.all()
  except Post.DoesNotExist:
    raise Http404
  return render_to_response("blog/single.html", {
                                            'media_url':MEDIA_URL,
                                            'post':post, 
                                            'images':images,
                                            'user':request.user,
                                            'months':mkmonth_lst(), 
                                            'archive':True,
                                             },
                                             context_instance=RequestContext(request))

def getCategory(request, categorySlug, selected_page=1):
    # Get specified category
    posts = Post.objects.all().order_by('-created')
    category_posts = []
    for post in posts:
        if post.categories.filter(slug=categorySlug):
            category_posts.append(post)

    # Add pagination
    pages = Paginator(category_posts, 5)

    # Get the category
    category = Category.objects.filter(slug=categorySlug)[0]

    # Get the specified page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display all the posts
    return render_to_response("blog/category_list.html", { 'posts': posts, 'page': returned_page, 'category': category})

def getList (request,year=0,month=0):
  if year == 0:
    all_posts = Post.objects.all().order_by('-created')
  else :
    all_posts = Post.objects.filter(created__year=year,created__month=month).order_by('-created')


  template = loader.get_template('blog/list.html')
  context= Context({'posts':all_posts,'months':mkmonth_lst()})
  return HttpResponse(template.render(context))


class PostsFeed(Feed):
    title = "My Django Blog posts"
    link = "feeds/posts/"
    description = "Posts from My Django Blog"

    def items(self):
        return Post.objects.order_by('-created')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text
