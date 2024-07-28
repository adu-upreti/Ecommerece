from django.shortcuts import render
from product.models import *



def Home(request):
    product_list = Products.objects.all()
    category_list = Category.objects.all()

    datas={
        
        'categories':category_list,
        'products':product_list,
       
    }

    return render(request, "user/index.html",datas)