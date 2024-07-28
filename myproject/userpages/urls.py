from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [


    path('about/', views.ABOUT,name='about-us'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart,name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.CONTACT,name='contactus'),
    path('product/', views.PRODUCT,name='productform'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)