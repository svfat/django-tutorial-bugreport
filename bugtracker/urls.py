# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import BugListView

urlpatterns = patterns('',
    url(r'^$', BugListView.as_view(), name='index'),
)
