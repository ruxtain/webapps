#! /Users/michael/anaconda3/bin/python
# @Date:   2018-09-01 10:22:06

from django.conf.urls import url
from app import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^vote', views.vote, name='vote'),
    url(r'^ladder', views.ladder, name='ladder'),
]
