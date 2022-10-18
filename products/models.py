from django.db import models
from operator import mod
from unicodedata import decimal
from unittest.util import _MAX_LENGTH

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/%code', height_field='200', width_field='100', max_length=2500)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='images/%code', height_field='200', width_field='100', max_length=2500)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    
    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")

    def __str__(self):
        return self.name