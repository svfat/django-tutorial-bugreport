# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import BugListView, BugDetailView, RegisterView, BugCreateView
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
    url(r'^$', BugListView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', BugDetailView.as_view(), name='detail'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login',
          {"template_name" : "login.html"}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
          {"next_page" : reverse_lazy('login')}, name="logout"),
    url(r'^add/$', BugCreateView.as_view(), name='add'),
)
