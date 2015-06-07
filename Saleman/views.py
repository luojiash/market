# coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from mymodel.models import Goods,SalesRecord,Staff
import datetime

# Create your views here.

def show_personal_info(request):
	errors = []
	nickname = request.user.username
	try:
		per = Staff.objects.get(Nickname=nickname)
	except Staff.DoesNotExist:
		errors.append('个人信息不存在，请点击“完善个人信息”！')
	if errors:
		return render_to_response('saleman_personal_info.html',{'errors':errors})
	else:
		return render_to_response('saleman_personal_info.html',{'per':per})

def add_personal_info_form(request):
    return render_to_response('saleman_add_personal_info_form.html')
	
def add_personal_info(request):
	nickname = request.user.username
	name = request.POST['name']
	sex = request.POST['sex']
	age = request.POST['age']
	position = request.POST['position']
	address = request.POST['address']
	phonenum = request.POST['phonenum']
	s = Staff(Name = name,
			 Sex = sex,
			 Age = age,
			 Position = position,
			 Address = address,
			 PhoneNum = phonenum,
			 Nickname = nickname)
	s.save()
	return HttpResponseRedirect('/accounts/saleman_show_personal_info')
	
def modify_personal_info_form(request):
    return render_to_response('saleman_modify_personal_info_form.html')
	
def modify_personal_info(request):
	nickname = request.user.username
	name = request.POST['name']
	sex = request.POST['sex']
	age = request.POST['age']
	position = request.POST['position']
	address = request.POST['address']
	phonenum = request.POST['phonenum']
	s = Staff.objects.get(Nickname = nickname)
	s.Name = name
	s.Sex = sex
	s.Age = age
	s.Position = position
	s.Address = address
	s.PhoneNum = phonenum
	s.Nickname = nickname
	s.save()
	return HttpResponseRedirect('/accounts/saleman_show_personal_info')

