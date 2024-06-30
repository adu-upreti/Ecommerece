
from django.shortcuts import render
from django.http import HttpResponse
from account.models import Accounts





def AccountSave(request):
    # print(request.POST.items)    print in terminal
    a_name = request.POST['name']
    a_phone = request.POST['phone']
    a_email = request.POST['email']
    a_image = request.FILES['image']
    a_category = request.POST['category']
    a_password = request.POST['password']
    a_password2 = request.POST['password2']



    Accounts.objects.create(name=a_name,phone=a_phone,email=a_email,image=a_image,category_id=a_category,password=a_password,password2=a_password2)
    
    return HttpResponse(f"submit details hass been saved: {a_name},{a_email},{a_phone}")

def AccountForm(request):
    data = {

        'dashboard_active_page':'active',
    }
    return render(request,'adminfile/accounts.html',data)
