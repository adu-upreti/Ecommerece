from django import forms



class Category(forms.Form):
   cat_name = forms.CharField(max_length = 200)


#    def __str__(self):
#         return self.cat_name



class Product_Form(forms.Form):

    name = forms.CharField(max_length = 1000)
    # image = forms.ImageField(upload_to='product/image',null=True)
    description = forms.CharField(max_length=50)
    price = forms.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = forms.IntegerField()
    category = forms.ForeignKey(Category,on_delete=forms.CASCADE,null=True,related_name = "catproducts")
    # (Category,on_delete=forms.CASCADE,null=True)



    # def __str__(self):
    #  return self.name