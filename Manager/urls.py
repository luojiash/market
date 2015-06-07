from django.conf.urls import patterns, include, url
from Manager import views
import os

urlpatterns = patterns('',
    url(r'^Sales/$', views.manage_page),
    url(r'^Sales_Inquiry/$', views.Sales_Inquiry),
    url(r'^show/$', views.show_goods),
    url(r'^update/(?P<pk>\d+)/$', views.update_goods.as_view()),
)
