from django import forms
from .models import Products,Category


class product_form(forms.ModelForm):
        class Meta:
         model = Products
         fields = "__all__"



class category_form(forms.ModelForm):
        class Meta:
         model = Category
         fields = "__all__"
