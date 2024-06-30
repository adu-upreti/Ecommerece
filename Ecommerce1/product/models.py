from django.db import models

# Create your models here.

class Category(models.Model):
   cat_name = models.CharField(max_length = 200)


   def __str__(self):
        return self.cat_name
   


class Products(models.Model):

    name = models.CharField(max_length = 1000)
    image = models.ImageField(upload_to='product/image',null=True)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name = "catproducts")
    # (Category,on_delete=models.CASCADE,null=True)



    def __str__(self):
     return self.name
