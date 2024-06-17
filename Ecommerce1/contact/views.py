from django.shortcuts import render
from django.http import HttpResponse
from contact.models import Contact

# Create your views here.


def SaveContact(request):
    C_email = request.POST['email']
    C_name = request.POST['name']
    C_message = request.POST['message']

    Contact.objects.create(email=C_email,name=C_name,message=C_message)
    
    return HttpResponse(f"your contact hass been saved {C_email},{C_name},{C_message}")



def MyContact(request):
    return render(request,"contact.html")  

