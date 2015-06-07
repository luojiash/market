# coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from mymodel.models import Goods,StockRecord,Staff
import datetime

# Create your views here.
@login_required(login_url='/accounts/login')
def add_existent_Goods_form(request):
    return render_to_response('add_existent_Goods_form.html')

@login_required(login_url='/accounts/login')
def add_existent_Goods(request):
    errors = []
    if 'name' in request.POST and 'count' in request.POST:
        name = request.POST['name']
        count = request.POST['count']
        purchasingPrice = request.POST['PurchasingPrice']
        if not name:
            errors.append('请输入商品名称！')
        elif not count:
            errors.append('请输入进货数量！')
        elif not purchasingPrice:
            errors.append('请输入进货价！')
        else:
            try:
                g = Goods.objects.get(Name=name)
            except Goods.DoesNotExist:
                errors.append('商品不存在，请核实后重新输入！')
            else:
                cur_count = g.Inventory
                g.Inventory = cur_count + int(count)
                g.save()
                r = StockRecord(Good_id = g,
                                Date = datetime.datetime.now().date(),
                                Count = count,
                                Price = purchasingPrice)
                r.save()
                if request.POST.has_key("continue"):
                    return HttpResponseRedirect('/accounts/add_existent_Goods_form')
                else:
                    return render_to_response('add_Goods_success.html')
        return render_to_response('add_existent_Goods_form.html',{'errors': errors})

@login_required(login_url='/accounts/login')
def add_new_Goods_form(request):
    return render_to_response('add_new_Goods_form.html')

@login_required(login_url='/accounts/login')
def add_new_Goods(request):
    errors = []
    if 'name' in request.POST and 'count' in request.POST:
        name = request.POST['name']
        count = request.POST['count']
        gtype = request.POST['type']
        sellingPrice = request.POST['SellingPrice']
        purchasingPrice = request.POST['PurchasingPrice']
        if not name:
            errors.append('请输入商品名称！')
        elif not count:
            errors.append('请输入进货数量！')
        elif not gtype:
            errors.append('请输入商品类别！')
        elif not purchasingPrice:
            errors.append('请输入商品进价！')
        elif not sellingPrice:
            errors.append('请输入商品售价！')
        else:
            g = Goods(Name = name,
                     Type = gtype,
                     SellingPrice = sellingPrice,
                     Inventory = count)
            g.save()
            r = StockRecord(Good_id = g,
                            Date = datetime.datetime.now().date(),
                            Count = count,
                            Price = purchasingPrice)
            r.save()
            if request.POST.has_key("continue"):
                return HttpResponseRedirect('/accounts/add_new_Goods_form')
            else:
                return render_to_response('add_Goods_success.html')
        return render_to_response('add_new_Goods_form.html',{'errors': errors})

def show_personal_info(request):
	errors = []
	nickname = request.user.username
	try:
		per = Staff.objects.get(Nickname=nickname)
	except Staff.DoesNotExist:
		errors.append('个人信息不存在，请点击“完善个人信息”！')
	if errors:
		return render_to_response('buyer_personal_info.html',{'errors':errors})
	else:
		return render_to_response('buyer_personal_info.html',{'per':per})

def add_personal_info_form(request):
    return render_to_response('buyer_add_personal_info_form.html')
	
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
	return HttpResponseRedirect('/accounts/buyer_show_personal_info')
	
def modify_personal_info_form(request):
    return render_to_response('buyer_modify_personal_info_form.html')
	
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
	return HttpResponseRedirect('/accounts/buyer_show_personal_info')

