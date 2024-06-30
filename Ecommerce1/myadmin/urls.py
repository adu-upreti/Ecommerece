
from django.urls import path
from . import views
urlpatterns=[
    path('login/',views.Login,name='Login'),
    path('logout',views.Logout,name="logout_admin"),
    path('',views.index,name='admin_dashboard'),
    path('products/',views.A_product,name="admin_product"),
    

    # path('product-form/',views.addProduct),
 
]
