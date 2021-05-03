from django.db import models
from empresa.models import Empresa
# Create your models here.
from django.contrib.auth.models import User
   
class Integrante(models.Model):
    nombres   = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    correo    = models.EmailField('email addres', unique=True)
    cedula    = models.IntegerField(blank=True, null=True)
    num_telf  = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=150)
    abilidad  = models.CharField(max_length=30)
    user      = models.ForeignKey(User, related_name='Integrante', null=False, blank=False,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
            ordering = ["nombres"]

    def __str__(self):
        return self.nombres

 