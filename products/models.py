from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table= "categories"
        verbose_name="Categoría"
        verbose_name_plural="Categorías"
        ordering=["-id"]

class Product(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productsImages')
    with_discount = models.BooleanField(null=True)

    class Meta:
        db_table= "products"
        verbose_name = ("product")
        verbose_name_plural = ("products")
        ordering=["id"]
        
    def __str__(self):
        return self.name
 