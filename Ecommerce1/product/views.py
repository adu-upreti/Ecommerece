from django.shortcuts import render
from django.http import HttpResponse
from product.models import Products



def ProductSave(request):
    # print(request.POST.items)    print in terminal
    p_name = request.POST['name']
    p_description = request.POST['description']
    p_expire_date = request.POST['expire_date']
    p_image = request.FILES['image']
    p_category = request.POST['category']
    p_stock = request.POST['stock']



    Products.objects.create(name=p_name,expire_date=p_expire_date,description=p_description,image=p_image,category=p_category,stock=p_stock)
    
    return HttpResponse(f"submit details hass been saved: {p_name},{p_stock},{p_description}")

def ProductForm(request):
    return render(request,'admin/add-product.html')

