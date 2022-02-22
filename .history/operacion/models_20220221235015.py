from django.db import models
from authapp.models import MyUser as User
from empresa.models import Empresa
from referencia.models import Referencia
from color.models import Color
# Create your models here.
class Operacion(models.Model):
    btnInfo       = '<button type="button" class="btn btn-outline-info text-center btn-sm btn-block ">Info</button>'
    btnAccion     = '<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>'
    ESTATUS       = (('A','Activo'),('I','Inactivo'))
    
    usuario       = models.ForeignKey(User, related_name='Operacion', null=True, blank=True,on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa, related_name='Operacion', null=False, blank=False,on_delete=models.CASCADE)
    referencia    = models.ForeignKey(Referencia, related_name='Operacion', null=True, blank=True,on_delete=models.CASCADE)
    color         = models.ForeignKey(Color, related_name='Operacion', null=False, blank=False,on_delete=models.CASCADE)
    nom_operacion = models.CharField(max_length=20, unique=True)
    nota          = models.CharField(max_length=50,blank=True, null=True)
    estatus       = models.CharField(max_length=1,choices=ESTATUS)
    can_total     = models.IntegerField(blank=True, null=True)
    can_restant
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    btnAcci = models.CharField(max_length=300, blank=True ,default=btnAccion , null=True)
    btnInfo = models.CharField(max_length=300, blank=True ,default=btnInfo , null=True)



    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]

    def __str__(self):
        return '%s %s %s %s %s %s %s %s' % (self.id, self.usuario, self.empresa,self.referencia,self.estatus,self.color,self.nom_operacion,self.created_at)
