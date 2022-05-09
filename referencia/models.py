from django.db import models
from authapp.models import MyUser as User
from empresa.models import Empresa
# Create your models here.

class Referencia(models.Model):
    ESTATUS        = (('A','Activo'),('I','Inactivo'))
    usuario        = models.ForeignKey(User, related_name='Referencia',on_delete=models.CASCADE)
    empresa        = models.ForeignKey(Empresa, related_name='Referencia',on_delete=models.CASCADE)
    nom_referencia = models.CharField(max_length=30)
    descripcion    = models.CharField(max_length=50)
    estatus        = models.CharField(max_length=1,choices=ESTATUS)
    
    #fotoPrendaUno = models.ImageField(upload_to='uploads/',null=False,blank=True ,height_field=None, width_field=None, max_length=100)
    #fotoPrendaDos = models.ImageField(upload_to='uploads/',null=False,blank=True ,height_field=None, width_field=None, max_length=100)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.id, self.nom_referencia, self.descripcion,self.created_at,self.usuario,self.empresa)