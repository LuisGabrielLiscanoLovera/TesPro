from django.db import models
from authapp.models import MyUser
from empresa.models import Empresa
# Create your models here.

class Color(models.Model):
    usuario        = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    empresa        = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    nom_color      = models.CharField(max_length=20)
    codigo_color   = models.CharField(blank=True, null=True,max_length=25)    
    
    ESTATUS       = (('A','Activo'),('I','Inactivo'))
    estatus       = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]
    def __str__(self):
            return 'id:{} nom_color:{}  cod_empresa:{} estatus:{}'.format(self.id, self.nom_color, self.codigo_color,self.estatus)
  
 






