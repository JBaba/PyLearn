from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
""" . means here import from current packages """
from . import views

urlpatterns = [
    url(r'^blog/', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
    	template_name="blog/home.html")),
]