from django.conf.urls import url
""" . means here import from current packages """
from . import views

urlpatterns = [
	""" Here we are calling method 'index' which is located inside 'views.py' file """
    url(r'^$', views.index, name='index')
]
