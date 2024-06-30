from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate,decorators
from product.models import Products,Category
# from myadmin.forms import Product_Form

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

def addProduct(request):
    data = {
        'add_product_active_page':'active'
    }
    return render(request,"myadminfile/products.html",data)



# @login_required
# def addProduct(request):
#     data = {
#         'product_active_page': 'active',
#         'categories': Category.objects.all()
#     }

#     if request.method == "POST":
#         print("save product")

#         my_form = Product_Form(request.POST)
#         if my_form.is_valid():
#             my_form.save()
#             data['success_message'] = "Product added successfully.........."
#         else:
#             data['errors'] = my_form.errors

#     return render(request, "adminfile/add-product.html", data)




@login_required
def A_product(request):
    product_list = Products.objects.all()
    category_list = Category.objects.all()

    datas={
        
        'categories':category_list,
        'products':product_list,
        'product_admin':'active'
    }

   
    return render(request,"adminfile/products.html",datas)




