from django.db import models
from empresa.models import Empresa

# Create your models here.

class Integrante(models.Model):
    nombres   = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    correo    = models.EmailField('email addres', unique=True)
    cedula    = models.IntegerField(blank=True, null=True)
    num_telf  = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=150)
    abilidad  = models.CharField(max_length=30)
    empresa = models.ForeignKey(Empresa, null=False, blank=False,on_delete=models.CASCADE)
    
    
    class Meta:
            ordering = ["nombres"]

    def __str__(self):
        return self.nombres

 