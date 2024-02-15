from django.shortcuts import render, redirect

from .models import Category,Post,Tag, Comment

# Create your views here.


def home_page(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    
    data = {
        "categories":categories,
        "posts":posts
    }
    return render(request=request, template_name='index.html', context=data)


def detail(request, post_id):
    categories = Category.objects.all()
    post = Post.objects.get(id=post_id)
    
    if request.method == 'POST':
        name = request.POST.get("name")
        comment = request.POST.get("comment")
        if all([name,comment]):
            Comment.objects.create(
                author=name,
                comment=comment,
                post=post
            )
    
    
    return render(request,"detail.html", context={
        "post":post,
        "categories":categories
        })
    
