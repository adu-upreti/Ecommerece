from django import forms
from .models import Products,Category


class category_form(forms.ModelForm):
        class Meta:
         model = Category
         fields = "__all__"

class product_form(forms.ModelForm):
        class Meta:
         model = Products
         fields = "__all__"
         widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control validate', 'required': 'required'}),
            'description': forms.Textarea(attrs={'class': 'form-control validate', 'rows': 3, 'required': 'required'}),
            'category': forms.Select(attrs={'class': 'custom-select tm-select-accounts'}),
            'price': forms.NumberInput(attrs={'class': 'form-control validate', 'data-large-mode': 'true'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control validate', 'required': 'required'}),
        }


