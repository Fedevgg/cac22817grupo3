from django.db import models

# Create your models here.

class Product(models.Model):
 
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

