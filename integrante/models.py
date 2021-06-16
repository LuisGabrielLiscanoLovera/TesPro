from django.db import models
from empresa.models import Empresa
from authapp.models import MyUser as User

# Create your models here.
class Integrante(models.Model):
    usuario    = models.ForeignKey(User, related_name='Integrante', null=True, blank=True,on_delete  = models.CASCADE)
    empresa    = models.ForeignKey(Empresa, related_name='Integrante', null=False, blank=False,on_delete=models.CASCADE)
    SEXO       = (('M','Hombre'),('F','Mujer'))
    ESTATUS    = (('A','Activo'),('I','Inactivo'))
    
    estatus    = models.CharField(max_length=1,choices=ESTATUS)
    nombres    = models.CharField(max_length=30)
    apellidos  = models.CharField(max_length=30)
    sexo       = models.CharField(max_length=1,choices=SEXO)
   
    correo     = models.EmailField('Correo')
    cedula     = models.IntegerField(blank=True, null=True,unique=True)
    num_telf   = models.IntegerField(blank=True, null=True)
    direccion  = models.CharField(max_length=150)
    abilidad   = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
            ordering = ["nombres"]

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.id, self.usuario, self.empresa,self.sexo,self.estatus,self.nombres,self.apellidos,self.correo,self.cedula,self.num_telf,self.direccion,self.abilidad,self.created_at)