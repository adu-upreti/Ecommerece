"""
URL configuration for Ecommerce1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from.viwes import Home,About,A_product,Dashboard
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin-dashboard/',include('accounts.urls')),
    path('dashboard/',Dashboard,name='dashboard'),
    path('myadmin/products/',A_product,name="adminproduct"),
    path('products/' , include('product.urls')),
    # path('login/',include('alogin.urls')),







    path('admin/', admin.site.urls),
    path('',Home),
    path('contact/' , include('contact.urls')),
    # path('products/',Product),
    path('about/',About),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

