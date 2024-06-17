from django.urls import path
from .views import ProductSave,ProductForm

urlpatterns = [
    path('product-form/',ProductForm,name="product_form"),  
    path('product-save/',ProductSave,name="product_save")
]