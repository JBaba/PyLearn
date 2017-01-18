from django.conf.urls import url, include
""" . means here import from current packages """
from . import views

urlpatterns = [
    url(r'^blog/', views.blog, name='blog'),
]