from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Category,Post,Comment,Rating

from .utils import check_read_articles
# Create your views here.


def home_page(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    paginator = Paginator(posts, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    last_comments = Comment.objects.all().order_by("-id")[:10]
    
    data = {
        "categories":categories,
        "page_obj":page_obj,
        "last_comments":last_comments
    }
    return render(request=request, template_name='index.html', context=data)




def detail(request, post_id):
    categories = Category.objects.all()
    post = Post.objects.get(id=post_id)
    category = Category.objects.get(id=post.category.id)
    related_posts = Post.objects.filter(category=category).exclude(id__in=[0,post.id]).order_by("?")
    
    request.session.modified = True
    
    if post.id in check_read_articles(request):
        pass
    else:
        check_read_articles(request).append(post.id)
        post.views += 1
        post.save()
    
    if request.method == 'POST':
        name = request.POST.get("name")
        comment = request.POST.get("comment")
        if all([name,comment]):
            Comment.objects.create(
                author=name,
                comment=comment,
                post=post
            )
            messages.add_message(request,messages.SUCCESS, "Successfuly !")
        else:
            messages.add_message(request,messages.ERROR, "Wrong !")
            
    
    
    return render(request,"detail.html", context={
        "post":post,
        "categories":categories,
        "related_posts":related_posts})
    


def set_rating(request,value,post_id):
    post = Post.objects.get(id=post_id)
    value = int(value)
    # print(post, value)
    if all([post,value]):
        Rating.objects.create(
            post=post,
            value=value
        )
        messages.add_message(request, messages.SUCCESS, "Rating set")
    else:
        messages.add_message(request, messages.WARNING, "Rating not set")
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def category_list(request,category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category=category)
    last_comments = Comment.objects.all().order_by("-id")[:10]
    
    paginator = Paginator(posts, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,"index.html",context={"page_obj":page_obj,"last_comments":last_comments} )
    
    
def search(request):
    last_comments = Comment.objects.all().order_by("-id")[:10]
    query = request.GET.get("query")
    posts = Post.objects.filter(title__icontains=query)
    
    paginator = Paginator(posts, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, "index.html",context={"page_obj":page_obj,"last_comments":last_comments})