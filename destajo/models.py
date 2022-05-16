from django.db import models
from integrante.models import Integrante
from tarea.models import Tarea
from operacion.models import Operacion
from empresa.models import Empresa

# Create your models here.
from authapp.models import MyUser as User
class Destajo(models.Model):
    usuario       = models.ForeignKey(User, related_name='Destajo',on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa, related_name='DestajoE', on_delete=models.CASCADE)
    operacion     = models.ForeignKey(Operacion, related_name='Destajo',on_delete=models.CASCADE)
    tarea         = models.ForeignKey(Tarea, related_name='Destajo',on_delete=models.CASCADE)
    integrante    = models.ForeignKey(Integrante, related_name='Destajo',on_delete=models.CASCADE)
    cantidad      = models.IntegerField(blank=True, null=True)
    talla         = models.CharField(blank=True, null=True,max_length=5)

    ESTATUS       = (('A','Activo'),('I','Inactivo'))
    estatus       = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.integrante)
    