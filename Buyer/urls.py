from django.conf.urls import patterns, include, url
from Buyer import views
import os

urlpatterns = patterns('',
	url(r'^add_existent_Goods_form/$',  views.add_existent_Goods_form),
	url(r'^add_existent_Goods/$',  views.add_existent_Goods),
	url(r'^add_new_Goods_form/$',  views.add_new_Goods_form),
	url(r'^add_new_Goods/$',  views.add_new_Goods),
	url(r'^buyer_show_personal_info/$',  views.show_personal_info),
	url(r'^buyer_modify_personal_info/$',  views.modify_personal_info),
	url(r'^buyer_add_personal_info/$',  views.add_personal_info),
	url(r'^buyer_modify_personal_info_form/$',  views.modify_personal_info_form),
	url(r'^buyer_add_personal_info_form/$',  views.add_personal_info_form),
)
