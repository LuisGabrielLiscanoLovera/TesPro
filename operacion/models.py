from django.db import models
from authapp.models import MyUser as User
from empresa.models import Empresa
from referencia.models import Referencia
from color.models import Color
# Create your models here.
class Operacion(models.Model):
    btnAccion     = '<button type="button" class="btn btn-outline-info icofont-dollar-true text-center btn-sm btn-block">btn</button>'
    usuario       = models.ForeignKey(User, related_name='Operacion', null=True, blank=True,on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa, related_name='Operacion', null=False, blank=False,on_delete=models.CASCADE)
    referencia    = models.ForeignKey(Referencia, related_name='Operacion', null=True, blank=True,on_delete=models.CASCADE)
    color         = models.ForeignKey(Color, related_name='Operacion', null=False, blank=False,on_delete=models.CASCADE)
    nom_operacion = models.CharField(max_length=20, unique=True)
    ESTATUS=(('A','Activo'),('I','Inactivo'))
    nota      = models.CharField(max_length=50,blank=True, null=True)
    estatus       = models.CharField(max_length=1,choices=ESTATUS)
    can_total    = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    btnAcci = models.CharField(max_length=300, blank=True ,default=btnAccion , null=True)



    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.usuario, self.empresa,self.referencia,self.estatus,self.color,self.nom_operacion,self.created_at)

class Talla(models.Model):
    usuario       = models.ForeignKey(User, related_name='Talla', null=True, blank=True,on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa, related_name='Talla', null=False, blank=False,on_delete=models.CASCADE)
    nom_talla     = models.CharField(max_length=20, unique=True)
    nota          = models.CharField(max_length=50,blank=True, null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    num_talla     = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]

    def __str__(self):
        return '%s %s %s %s %s %s ' % (self.id, self.usuario, self.empresa,self.nom_talla,self.nota,self.created_at)
    
class CanTalla(models.Model):
    usuario       = models.ForeignKey(User, related_name='CanTalla', null=True, blank=True,on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa, related_name='CanTalla', null=False, blank=False,on_delete=models.CASCADE)
    can_talla     = models.IntegerField(blank=True, null=True)
    res_talla     = models.IntegerField(blank=True, null=True)
    talla         = models.ForeignKey(Talla, related_name='CanTalla', null=False, blank=False,on_delete  =models.CASCADE)
    operacion     = models.ForeignKey(Operacion, related_name='CanTalla', null=False, blank=False,on_delete=models.CASCADE)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]

    def __str__(self):
        return '%s %s %s %s %s %s %s %s ' % (self.id, self.usuario, self.empresa,self.can_talla,self.res_talla,self.talla,self.operacion,self.created_at)
    
