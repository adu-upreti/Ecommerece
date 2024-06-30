
from django.urls import path
from.views import MyContact,SaveContact

urlpatterns = [
    path('contact-us/',MyContact,name='contactus'),
    path('save-contact/',SaveContact,name='save_contact'),  
]


