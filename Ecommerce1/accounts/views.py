from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model,login,logout,authenticate


# Create your views here.

def Login(request):
    data = {
        'login_active_page':'active'
    }
    print(request.method, " this  is request method")

    if request.method == "GET":
       return render(request,"myadmin/login.html",data)
    elif request.method == "POST":
        form_username = request.POST['username']
        form_password = request.POST['password']
        # user_obj = get_user_model().objects.filter(username = form_username)
        # print(user_obj,"::",user_obj.first())
        user_obj = authenticate(username  = form_username,password = form_password)
        if user_obj:
            # pass
            login(request,user=user_obj)
            return index(request)
        else:
            return HttpResponse("Sorry your account is invalid")
    else:
        print("unknown")
 
    

def Logout(request):
    logout(request)
    data = {
        'logout_active_page':'active'
    }
    return render(request,"myadmin/login.html",data)

@login_required
def index(request):
    data = {
        'dashboard_active_page':'active'
    }
    return render(request,"myadmin/index.html",data)

def addProduct(request):
    data = {
        'add_product_active_page':'active'
    }
    return render(request,"myadmin/product_form.html",data)

@login_required
def getProduct(request):
    data = {
        'product_active_page':'active'
    }
    return render(request,"myadmin/products.html",data)

@login_required
def adminProfile(request):
    data = {
        'profile_active_page':'active'
    }
    return render(request,"myadmin/accounts.html",data)