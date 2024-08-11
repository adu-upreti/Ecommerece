from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from product.models import *
from product.forms import *


def user_dashboard(request):
    product_list = Products.objects.all()
    category_list = Category.objects.all()


    data = {
        'dashboard_active_page': 'active',
        'categories': category_list,
        'products': product_list,

    }
    return render(request, "user/index.html", data)






