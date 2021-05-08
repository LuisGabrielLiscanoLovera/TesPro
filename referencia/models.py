from django.db import models
from django.contrib.auth.models import User
from empresa.models import Empresa
# Create your models here.

class Referencia(models.Model):
    
    empresa           = models.ForeignKey(Empresa, related_name='Referencia', null=True, blank=True,on_delete=models.CASCADE)
    nom_referencia = models.CharField(max_length=20, unique=True)
    descripcion    = models.CharField(max_length=50)    
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["nom_referencia"]
    def __str__(self):
        return self.nom_referencia

 