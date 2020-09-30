from django.db import models

# Create your models here.

class PartidoPolitico(models.Model):
    logo=models.ImageField(upload_to="partidos")
    nombre=models.CharField(max_length=60)
    Abreviatura=models.CharField(max_length=60)
    numero=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural="Partidos Politicos"

