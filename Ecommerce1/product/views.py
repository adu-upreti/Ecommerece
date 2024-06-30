from django.shortcuts import render
from django.http import HttpResponseRedirect
from product.models import Category
from myadmin.forms import Product_Form






def ProductForm(request):
    data = {
        'product_active_page': 'active',
        'categories': Category.objects.all(),
    }

    # print(request.POST)
    if request.method == "POST":
        # print("save product")
        my_form = Product_Form(request.POST)
        
        if my_form.is_valid():
            HttpResponseRedirect("adminfile/add-product.html")
            # my_form.save()

            # data['success_message'] = "Product added successfully.........."

        else:
            form = Product_Form()
            # data['errors'] = my_form.errors

    return render(request, "adminfile/add-product.html",data,{"form":form})






# def ProductSave(request):
#     # print(request.POST.items)    print in terminal
#     p_name = request.POST['name']
#     p_description = request.POST['description']
#     p_price = request.POST.get('price')

#     p_image = request.FILES['image']
#     p_category = request.POST['category']
#     p_stock = request.POST['stock']



#     Products.objects.create(name=p_name,price=p_price,description=p_description,image=p_image,category_id=p_category,stock=p_stock)
    
#     return HttpResponse(f"submit details hass been saved: {p_name},{p_stock},{p_description}")


