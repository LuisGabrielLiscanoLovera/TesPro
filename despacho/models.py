from django.db import models
from operacion.models import Operacion
from patinador.models import Patinador
from empresa.models import Empresa
from authapp.models import MyUser as User
from talla.models import Talla
# Create your models here.

class Despacho(models.Model):
    usuario           = models.ForeignKey(User, null=True,blank=True,related_name='Despacho',on_delete=models.CASCADE)
    patinador         = models.ForeignKey(Patinador, related_name='Despacho', null=False, blank=False,on_delete=models.CASCADE)
    empresa           = models.ForeignKey(Empresa, related_name='Despacho', null=False, blank=False,on_delete=models.CASCADE)
    operacion         = models.ForeignKey(Operacion,related_name='Despacho',on_delete=models.CASCADE)
    talla             = models.ForeignKey(Talla,related_name='Despacho',null=True, blank=False,on_delete=models.CASCADE,db_constraint=False)
    can_terminada     = models.IntegerField(blank=True, null=True)
    
    #integrante = models.ForeignKey(Integrante,related_name='DespachoI', null=False, blank=False,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'id {} can_termin {} usuario {} empresa {}'.format(self.id, self.can_terminada,self.usuario,self.empresa)




class Task(models.Model):
    title = models.CharField(max_length=140)
    date  = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering=['completed','date']
        
        
        