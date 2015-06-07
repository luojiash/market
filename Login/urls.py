from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from Login import views
urlpatterns = patterns('',
    url(r'^login/$',  views.login),
    url(r'^logout/$', views.logout),
    url(r'^saleman_main/$',  views.saleman_main),
    url(r'^buyer_main/$',  views.buyer_main),
    url(r'^manager_main/$',  views.manager_main), 
)
