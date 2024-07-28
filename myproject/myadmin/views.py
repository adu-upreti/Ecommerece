from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate,decorators



def Login(request):
    data = {
        'login_active_page':'active'
    }

    if request.method == "GET":
       return render(request,"adminfile/login.html",data)
    
    elif request.method == "POST":
        form_username = request.POST['username']
        form_password = request.POST['password']
        user_obj = authenticate(username  = form_username,password = form_password)
        if user_obj:
            login(request,user=user_obj)
            return index(request)
        else:
            return render(request,"adminfile/login.html")
    else:
        print("unknown")
 
@login_required
def Logout(request):
    logout(request)
    data = {
        'logout_active_page':'active'
    }
    return render(request,"adminfile/login.html",data)

@login_required
def index(request):
    data = {
        'dashboard_active_page':'active'
    }
    return render(request,"adminfile/dashboard.html",data)




def register(request):
    
    return render(request, 'adminfile/accounts.html')