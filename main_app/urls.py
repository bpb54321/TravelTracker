from django.conf.urls import url
from . import views

urlpatterns = [
    # /
    url(r'^$', views.index)
]

# My name is Brian, and I am writing a comment in Django.
