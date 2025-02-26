from django.shortcuts import render
from django.http.response import HttpResponse
from work.models import Blog, Category


# Create your views here.
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request,"work/index.html",context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "work/blogs.html",context)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)

    return render(request, "work/blog-details.html", {
        "blog": blog
    })

def blogs_by_category(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
        
    }
    return render(request, "work/blogs.html",context)