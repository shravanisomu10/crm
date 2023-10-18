from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomerUser(models.Model):
    phone = models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    


