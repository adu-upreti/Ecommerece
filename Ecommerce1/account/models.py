
from django.db import models


   


class Accounts(models.Model):

    name = models.CharField(max_length = 1000)
    image = models.ImageField(upload_to='product/image',default='images/default.jpg')
    phone = models.IntegerField(20)
    email = models.EmailField()
    password = models.CharField(max_length = 10)
    password2 = models.CharField(max_length = 10)



    def __str__(self):
     return self.name
