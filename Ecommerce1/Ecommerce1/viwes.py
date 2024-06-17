from django.http import HttpResponse
from django.shortcuts import render





def Home(request):
    return render(request,"index.html")


def Single(request):
    return render(request,"single-product.html")

def About(request):
    return render(request,"about.html")




def Login(request):
    return render(request,"admin/login.html")
def A_product(request):
    return render(request,"admin/products.html")
def Dashboard(request):
    return render(request,"admin/dashboard.html")


