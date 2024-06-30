from django.http import HttpResponse
from django.shortcuts import render
from product.models import Products,Category





def Home(request):
    category_list = Category.objects.all()
    product_list  = Products.objects.all()
    datas={
        'categories':category_list, 
        'products':product_list
    }
    return render(request,"index.html",datas)


def Userpoducts(request):
    return render(request,"product.html")

def Single(request):
    return render(request,"single-product.html")

def About(request):
    return render(request,"about.html")
