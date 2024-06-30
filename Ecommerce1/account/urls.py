from django.urls import path
from .views import AccountSave,AccountForm

urlpatterns = [
    path('account-form/',AccountForm,name="account_form"),  
    path('account-save/',AccountSave,name="account_save"),
  
]
