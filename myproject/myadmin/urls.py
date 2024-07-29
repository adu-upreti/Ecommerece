from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views


urlpatterns = [

    path('',views.register, name="adminregister"),
    path('login/',views.Login,name="adminlogin"),
    path('logout/',views.Logout,name="adminlogout"),
    path('dashboard/',views.index,name="admin_dashboard"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)