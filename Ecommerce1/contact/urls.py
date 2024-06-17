
from django.urls import path
from.views import MyContact,SaveContact

urlpatterns = [
    path('contact-us/',MyContact,),
    path('save-contact/',SaveContact,name='save_contact'),  
]


