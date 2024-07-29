from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register, name='userregister'),
    path('login/', views.login, name='userlogin'),
    path('home/', views.user_home, name='user_home'),


    path('about/', views.ABOUT, name='about-us'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.CONTACT, name='contactus'),
    path('product/', views.PRODUCT, name='productform'),
    path('category/<int:category_id>/', views.category_products_view, name='category_product'),
    path('search/', views.product_search, name='product_search'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)