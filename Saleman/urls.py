from django.conf.urls import patterns, include, url
from Saleman import views
import os

urlpatterns = patterns('',
	url(r'^saleman_show_personal_info/$',  views.show_personal_info),
	url(r'^saleman_modify_personal_info/$',  views.modify_personal_info),
	url(r'^saleman_add_personal_info/$',  views.add_personal_info),
	url(r'^saleman_modify_personal_info_form/$',  views.modify_personal_info_form),
	url(r'^saleman_add_personal_info_form/$',  views.add_personal_info_form),
)
