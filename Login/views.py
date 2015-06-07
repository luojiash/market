from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required  
# from django.contrib.auth.views import login,logout
from django.contrib import auth

# Create your views here. 

def login(request):
    error = False
    if request.POST:
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.has_perm('mymodel.add_staff'):
                return HttpResponseRedirect('/accounts/manager_main')
            elif user.has_perm('mymodel.add_member'):
                return HttpResponseRedirect('/accounts/saleman_main')
            else:
                return HttpResponseRedirect('/accounts/buyer_main')
        else:
            error = True
    return render_to_response('login_form.html',{'error':error})

@login_required(login_url='/accounts/login')    
def manager_main(request):
    return render_to_response('manager_main.html',
            {'full_name':request.user.username})

@login_required(login_url='/accounts/login')    
def saleman_main(request):
    return render_to_response('saleman_main.html',
            {'full_name':request.user.username})

@login_required(login_url='/accounts/login')    
def buyer_main(request):
    return render_to_response('buyer_main.html',
            {'full_name':request.user.username})

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

