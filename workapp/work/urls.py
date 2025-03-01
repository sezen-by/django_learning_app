from django.urls import path
from . import views

#http://128.0.0.1:8000/         => homepage
#http://128.0.0.1:8000/index    => homepage
#http://128.0.0.1:8000/blogs    => blogs
#http://128.0.0.1:8000/blogs/3  => blog-details

urlpatterns = [
    path("", views.index,name="home"), #Çift tırnak 128.0.0.1:8000 oluyor.
    path("index", views.index), 
    path("blogs", views.blogs,name="blogs"),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("blogs/<slug:slug>", views.blog_details,name="blog_details"),
]