# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView#update
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger#分页显示
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from mymodel.models import Goods,SalesRecord,StockRecord
# Create your views here.

@login_required(login_url='/accounts/login')
def manage_page(request):
	Good = Goods.objects.all()
	return render_to_response('Sales_Inquiry.html',{'Goods':Good})

@login_required(login_url='/accounts/login')
def Sales_Inquiry(request):
	Inquiry = request.GET['ChooseInquiry']
	start_date = request.GET['start_date']
	end_date = request.GET['end_date']
	if Inquiry == 'AllSales' :
		salesrecords = SalesRecord.objects.filter(Date__range=(start_date,end_date))
		stockrecords = StockRecord.objects.filter(Date__range=(start_date,end_date))
		sellroom = cost = 0.0
		for i in salesrecords:
			sellroom += i.Price * i.Count
		for i in stockrecords:
			cost += i.Price * i.Count
		profit = cost - sellroom
		context = {'start_date':start_date,'end_date':end_date,'sellroom':sellroom,'cost':cost,'profit':profit}
		return render_to_response('Sales_Inquiry_All.html',context)
	else:
		good_type = request.GET['ChooseGood']
		Good_list = Goods.objects.filter(Type=good_type)
		item_list = []
		for good in Good_list:
			sellroom = sellnumber = 0.0

			salesrecords = SalesRecord.objects.filter(Date__range=(start_date,end_date),Good_id=good)
			for i in salesrecords:
				sellroom += i.Price * i.Count
				sellnumber += i.Count
			context = {'id':good.ID,'name':good.Name,'sellnumber':sellnumber,'sellroom':sellroom}
			item_list.append(context)
		return render_to_response('Sales_Inquiry_Part.html',{'start_date':start_date,'end_date':end_date,'item_list':item_list})

@login_required(login_url='/accounts/login')		
def show_goods(req):
    error = []
    q = req.GET.get('q')
    r = req.GET.get('r')
    comp = req.GET.get('comp')
    form = Goods.objects.all()
    if 'q' in req.GET or 'r' in req.GET:
        if not q and not r:
            error.append("input your keyword!")
        else:
            if r and not r.isdigit():
                error.append("invalid input!")
            else:
                if q:
                    qset = (Q(Name__icontains = q) | Q(Type__icontains = q))
                    form = form.filter(qset)
                if r:
                    if comp == 'less':
                        form = form.filter(Inventory__lte=r)
                    else:
                        form = form.filter(Inventory__gte=r)
    limit = 10
    pagi = Paginator(form, limit)
    page = req.GET.get('page','1')
    try:
        form = pagi.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        form = pagi.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        form = pagi.page(paginator.num_pages)  # 取最后一页的记录
    return render_to_response('show_goods.html',{'form':form,
                                'error':error,'q':q, 'comp':comp, 'r':r})

class update_goods(UpdateView):
    model = Goods
    template_name = 'update_goods.html'
    success_url = '/accounts/show/'
	

