from django.db import models

# Create your models here.

class Category(models.Model):
   cat_name = models. CharField(max_length = 200)


def __str__(self):
 return self.cat_name
   


class Products(models.Model):

    name = models.CharField(max_length = 1000)
    image = models.ImageField(upload_to='product/image',null=True)
    description = models.CharField(max_length=50)
    expire_date = models.CharField(max_length=12)
    category = models.CharField(max_length=12)
    stock = models.IntegerField()
    category = models.ManyToManyField(Category)



    def __str__(self):
     return self.name
