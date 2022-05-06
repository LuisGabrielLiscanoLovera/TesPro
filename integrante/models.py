from django.db import models
from empresa.models import Empresa
from authapp.models import MyUser as User



# Create your models here.
class Integrante(models.Model):
    usuario    = models.ForeignKey(User, related_name='Integrante', on_delete  = models.CASCADE)
    empresa    = models.ForeignKey(Empresa, related_name='Integrante', null=False, blank=False,on_delete  = models.CASCADE)
    SEXO       = (('H','Hombre'),('M','Mujer'),('O','Otro'))
    ESTATUS    = (('A','Activo'),('I','Inactivo'))
    
    estatus    = models.CharField(max_length=1,choices=ESTATUS)
    nombres    = models.CharField(max_length=30)
    apellidos  = models.CharField(max_length=30)
    sexo       = models.CharField(max_length=1,choices=SEXO)
    cedula     = models.IntegerField()
    correo     = models.EmailField('Correo',blank=True, null=True)
    
    num_telf   = models.IntegerField(blank=True, null=True)
    direccion  = models.CharField(blank=True, null=True, max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    btnInfo = models.CharField(max_length=100, blank=True ,default='<button type="button" class="btn btn-outline-info text-center btn-sm btn-block">Info</button>', null=True)
    btnAcci = models.CharField(max_length=100, blank=True ,default='<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>' , null=True)
    
    class Meta:
            ordering = ["nombres"]

    def __str__(self):#return f"{self.nombres}"
        return '%s %s %s %s %s %s %s %s %s %s %s %s' % (self.id, self.usuario, self.empresa,self.sexo,self.estatus,self.nombres,self.apellidos,self.correo,self.cedula,self.num_telf,self.direccion,self.created_at)