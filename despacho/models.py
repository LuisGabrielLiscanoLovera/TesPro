from django.db import models
from prenda.models import Prenda
from integrante.models import Integrante
# Create your models here.
class Despacho(models.Model):
    prenda        = models.ForeignKey(Prenda,related_name='Despacho',on_delete=models.CASCADE)
    can_terminada = models.IntegerField(blank=True, null=True)
    integrante = models.ForeignKey(Integrante,related_name='Despacho', null=False, blank=False,on_delete=models.CASCADE)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    
    def __str__(self):
        return str(self.prenda)
