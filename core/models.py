from django.db import models

# Create your models here.

class Contact(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.SmallIntegerField()
    correo = models.EmailField(max_length=254)
    solicitud = models.TextField()

    def __str__(self):
        return self.nombre