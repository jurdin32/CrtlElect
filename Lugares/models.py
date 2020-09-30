from django.db import models

# Create your models here.
class Provincia(models.Model):
    nombre=models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    provincia=models.ForeignKey(Provincia,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural="Ciudades"