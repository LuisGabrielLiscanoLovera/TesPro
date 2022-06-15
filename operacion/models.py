from django.db import models
from authapp.models import MyUser
from empresa.models import Empresa
from referencia.models import Referencia
from color.models import Color
# Create your models here.
class Operacion(models.Model):
    btnInfo       = '<button type="button" class="btn btn-outline-info text-center btn-sm btn-block ">Info</button>'
    btnAccion     = '<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>'
    
    costeProd     = models.IntegerField(blank=True, null=True, default=0)
    usuario       = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    referencia    = models.ForeignKey(Referencia, on_delete=models.CASCADE,blank=True, null=True)
    color         = models.ForeignKey(Color, on_delete=models.CASCADE,blank=True, null=True)
    nom_operacion = models.CharField(max_length=35)
    nota          = models.CharField(max_length=150,blank=True, null=True)
    can_total     = models.IntegerField(blank=True, null=True)
    can_restante  = models.IntegerField(blank=True, null=True)    
    btnAcci       = models.CharField(max_length=300,default=btnAccion , null=True)
    btnInfo       = models.CharField(max_length=300,default=btnInfo , null=True)
        
    ESTATUS       = (('A','Activo'),('I','Inactivo'))
    estatus       = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    fecha_cierre  = models.DateTimeField(blank=True,null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]

    def __str__(self):
        return 'id:{} usuario:{} empresa:{} referencia:{} color:{} nom_operacion:{} created_at:{} estatus:{} '.format(self.id, self.usuario,
        self.empresa,self.referencia,
        self.color,
        self.nom_operacion,self.created_at,
        self.estatus)
