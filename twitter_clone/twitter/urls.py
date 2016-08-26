from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home), # User home page
    url(r'^(?P<username>[a-z]+)/$', views.profile),# User profile
]
