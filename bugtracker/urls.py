# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import BugListView, BugDetailView, RegisterView

urlpatterns = patterns('',
    url(r'^$', BugListView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', BugDetailView.as_view(), name='detail'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
)
