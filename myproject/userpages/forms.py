from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistrationForm(UserCreationForm):
    email = forms.forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)


    class Meta:
        model = Customuser
        fields = ['username', 'email', 'phone', 'password1', 'password2']



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


