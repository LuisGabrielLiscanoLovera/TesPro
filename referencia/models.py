from django.db import models
from authapp.models import MyUser as User
from empresa.models import Empresa
# Create your models here.

class Referencia(models.Model):
    usuario        = models.ForeignKey(User, related_name='Referencia', null=True, blank=True,on_delete=models.CASCADE)
    empresa        = models.ForeignKey(Empresa, related_name='Referencia', null=True, blank=True,on_delete=models.CASCADE)
    nom_referencia = models.CharField(max_length=20, unique=True)
    descripcion    = models.CharField(max_length=50)
    fotoPrendaUno  = models.ImageField(upload_to='uploads/',null=False,blank=True ,height_field=None, width_field=None, max_length=100)
    fotoPrendaDos  = models.ImageField(upload_to='uploads/',null=False,blank=True ,height_field=None, width_field=None, max_length=100)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.id, self.nom_referencia, self.descripcion,self.created_at,self.usuario,self.empresa)



