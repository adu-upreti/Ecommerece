from django.db import models
from django.contrib.auth.models import AbstractUser

class Customuser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
