from django.db import models
from referencia.models import Referencia
from color.models import Color

# Create your models here.
from django.contrib.auth.models import User

class Prenda(models.Model):
    #falta color
    referencia      = models.ForeignKey(Referencia, related_name='Prenda', null=False, blank=False,on_delete=models.CASCADE)
    color           = models.ForeignKey(Color, related_name='Prenda',on_delete=models.CASCADE)

    ESTATUS=(
        ('A','Activo'),
        ('C','Cerrado')
    )
    
    estutus       = models.CharField(max_length=1,choices=ESTATUS)
    nom_operacion = models.CharField(max_length=20, unique=True)
    estado        = models.CharField(max_length=20)
    cant_total    = models.IntegerField(blank=True, null=True)
    cant_tallaS   = models.IntegerField(blank=True, null=True)
    cant_tallaM   = models.IntegerField(blank=True, null=True)
    cant_tallaL   = models.IntegerField(blank=True, null=True)
    cant_tallaXL  = models.IntegerField(blank=True, null=True)
    cant_tallaXXL = models.IntegerField(blank=True, null=True)
    rS            = models.IntegerField(blank=True, null=True)
    rM            = models.IntegerField(blank=True, null=True)
    rL            = models.IntegerField(blank=True, null=True)
    rXL           = models.IntegerField(blank=True, null=True)
    rXXL          = models.IntegerField(blank=True, null=True)
    nota          = models.CharField(max_length=50,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
            ordering = ["nom_operacion"]

    def __str__(self):
        return self.nom_operacion
