from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [

    
    path('login/',views.Login,name="adminlogin"),
    path('logout/',views.Logout,name="adminlogout"),
    path('admin-dashboard/',views.admin_dashboard,name="admin_dashboard"),
    path('signup/',views.register, name="adminregister"),
    path('forget/',views.Forget_pass, name='forget')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)