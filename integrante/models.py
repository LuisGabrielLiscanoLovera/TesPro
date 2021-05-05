from django.db import models
from empresa.models import Empresa
from django.contrib.auth.models import User
# Create your models here.
class Integrante(models.Model):
    empresa           = models.ForeignKey(Empresa, related_name='Integrante', null=False, blank=False,on_delete=models.CASCADE)
    SEXO=(('M','Hombre'),('F','Mujer'))
    ESTATUS=(('A','Activo'),('I','Inactivo'))
    estutus       = models.CharField(max_length=1,choices=ESTATUS)
    sexo       = models.CharField(max_length=1,choices=SEXO)
    nombres   = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    correo    = models.EmailField('Correo', unique=True)
    cedula    = models.IntegerField(blank=True, null=True)
    num_telf  = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=150)
    abilidad  = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
            ordering = ["nombres"]

    def __str__(self):
        return self.nombres

 