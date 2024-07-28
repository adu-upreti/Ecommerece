from django.shortcuts import render, get_object_or_404, redirect
from product.models import *


 


def ABOUT(request):

    return render(request, "user/about.html") 


def add_to_cart(request, product_id):
    CartItem.objects.all().delete()

    product = get_object_or_404(Products, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'user/cart.html', {'cart_items': cart_items, 'total': total})


def CONTACT(request):

    return render(request, "user/contact.html") 


def PRODUCT(request):

    return render(request, "user/product.html") 
