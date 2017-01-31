from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.mainview, name='mainview'),
    url(r'^project/(?P<pk>[0-9]+)/$', views.projectview, name='project'),
    url(r'^complete/(?P<pk>[0-9]+)/$', views.completetask, name='complete'),
    url(r'^remove/(?P<pk>[0-9]+)/$', views.removeproj, name='removeproj'),

    ]
