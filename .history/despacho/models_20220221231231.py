from django.db import models
from operacion.models import Operacion
from integrante.models import Integrante
from empresa.models import Empresa
from authapp.models import MyUser as User
from talla.models import Talla
# Create your models here.

class Despacho(models.Model):
    usuario           = models.ForeignKey(User, null=True,blank=True,related_name='Despacho',on_delete=models.CASCADE)
    empresa           = models.ForeignKey(Empresa, related_name='DespachoE', null=False, blank=False,on_delete=models.CASCADE)
    talla             = models.ForeignKey(Talla,related_name='')
    nom_patinador     = models.OneToOneField(Integrante, related_name='DespachoPP', null=False, blank=False,on_delete=models.CASCADE)
    operacion         = models.ForeignKey(Operacion,related_name='DespachoO',on_delete=models.CASCADE)
    can_terminada     = models.IntegerField(blank=True, null=True)
    
    #integrante = models.ForeignKey(Integrante,related_name='DespachoI', null=False, blank=False,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.operacion)

