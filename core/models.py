from django.db import models

# Create your models here.

class Contact(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
#    edad = models.SmallIntegerField()
    correo = models.EmailField(max_length=254)
    consulta = models.TextField()

    class Meta:
        db_table= "consultas"
        verbose_name="consulta"
        verbose_name_plural="consultas"
        ordering=["-id"]

    def __str__(self):
        return self.nombre