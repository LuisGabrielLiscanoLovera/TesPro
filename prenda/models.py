from django.db import models
from referencia.models import Referencia
# Create your models here.
class Prenda(models.Model):
    #falta color
    nom_operacion = models.CharField(max_length=20, unique=True)
    referencia    = models.CharField(max_length=20)    
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
    nota          = models.CharField(max_length=50)
    referencia    = models.ForeignKey(Referencia, related_name='Prenda',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
            ordering = ["nom_operacion"]

    def __str__(self):
        return self.nom_operacion
