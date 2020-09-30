from django.db import models

# Create your models here.
from Elecciones.models import PartidoPolitico
from Lugares.models import Provincia

DIGNIDAD=(
    ("Presidente","Presidente"),
    ("Asambleista Nacional","Asambleista Nacional"),
    ("Asambleista Provincial","Asambleista Provincial"),
    ("Parlamentario Andino","Parlamentario Andino")
)

class Dignidad(models.Model):
    partido=models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)
    dignidad=models.CharField(max_length=60, choices=DIGNIDAD)
    nombre=models.CharField(max_length=60,null=True,blank=True)
    provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE,null=True,blank=True)


