from django.db import models
from operacion.models import Operacion
from integrante.models import Integrante
from empresa.models import Empresa

# Create your models here.
from django.contrib.auth.models import User

class Despacho(models.Model):
    empresa           = models.ForeignKey(Empresa, related_name='DespachoE', null=False, blank=False,on_delete=models.CASCADE)
    nom_patinador     = models.OneToOneField(Integrante, related_name='DespachoPP', null=False, blank=False,on_delete=models.CASCADE)
    operacion         = models.ForeignKey(Operacion,related_name='DespachoO',on_delete=models.CASCADE)
    can_terminada = models.IntegerField(blank=True, null=True)
    #integrante = models.ForeignKey(Integrante,related_name='DespachoI', null=False, blank=False,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.operacion)

