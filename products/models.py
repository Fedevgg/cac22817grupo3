from django.db import models

# Create your models here.

class Product(models.Model):
    codename = ''
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productsImages')

#    if brand == 'Philips':
#        codename = '{0}{1}'.format('001',id)
#    elif brand == 'HP':
#        codename = '{0}{1}'.format('002',id)
#    else: 
#        codename = '{0}{1}'.format('003',id)

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):
        return self.name
