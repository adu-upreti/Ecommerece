from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from product.models import *
from .forms import * 
from django.contrib.auth.models import User

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib import messages


def Login(request):
    data = {
        'login_active_page':'active'
    }

    if request.method == "GET":
        return render(request, "adminfile/login.html", data)
    
    elif request.method == "POST":
        form_username = request.POST['username']
        form_password = request.POST['password']
        user_obj = authenticate(username=form_username, password=form_password)
        if user_obj:
            login(request, user=user_obj)
            if user_obj.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            return render(request, "adminfile/login.html", {'error': 'Invalid credentials'})
    else:
        print("unknown")

@login_required
def Logout(request):
    logout(request)
    data = {
        'logout_active_page':'active'
    }
    return render(request, "adminfile/login.html", data)




@login_required
def admin_dashboard(request):
    data = {
        'dashboard_active_page': 'active'
    }
    return render(request, "adminfile/dashboard.html", data)



def register(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'adminfile/register.html', {'error': 'Username already exists'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'adminfile/register.html', {'error': 'Email already exists'})
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('adminlogin')
        else:
            return render(request, 'adminfile/register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'adminfile/register.html')



def Forget_pass(request):

    return render(request, 'adminfile/forget.html')




def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = 'forget.html'
                    c = {
                        'email': user.email,
                        'domain': request.META['HTTP_HOST'],
                        'site_domain': 'Your Site',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    send_mail(subject, email, 'admin@yourdomain.com', [user.email], fail_silently=False)
                messages.success(request, 'A password reset link has been sent to your email.')
                return redirect("adminlogin")
            else:
                messages.error(request, 'No account found with this email address.')
    else:
        form = PasswordResetForm()
    return render(request, "password_reset.html", {"form": form})