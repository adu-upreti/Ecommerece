from django.shortcuts import render
from django.http import HttpResponse
from .forms import product_form
# from .models import Category

def ProductForm(request):
    # data = {
    #     'product_active_page': 'active',
    #     'categories': Category.objects.all(),
    # }
    print(request.POST.items)
    if request.method == "POST":
        print(request.FILES)
        form = product_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Product is saved.")
        else:
            print(form.errors)
    else:
        
        form = product_form()

    return render(request, "adminfile/add-product.html", {"form": form})





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


