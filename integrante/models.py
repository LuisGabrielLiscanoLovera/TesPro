from django.db import models
from empresa.models import Empresa
from authapp.models import MyUser 
# Create your models here.
class Integrante(models.Model):
    usuario = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    empresa    = models.ForeignKey(Empresa,  on_delete  = models.CASCADE)
    SEXO       = (('H','Hombre'),('M','Mujer'),('O','Otro'))   
    nombres    = models.CharField(max_length=30)
    apellidos  = models.CharField(max_length=30)
    sexo       = models.CharField(max_length=1,choices=SEXO)
    cedula     = models.IntegerField(unique=True)
    correo     = models.EmailField('Correo',blank=True, null=True)    
    num_telf   = models.CharField(blank=True, null=True,max_length=15)
    direccion  = models.CharField(blank=True, null=True, max_length=250)
    btnInfo = models.CharField(max_length=100,default='<button type="button" class="btn btn-outline-info text-center btn-sm btn-block">Info</button>')
    btnAcci = models.CharField(max_length=100, default='<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>')
    ESTATUS       = (('A','Activo'),('I','Inactivo'))
    estatus       = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
            ordering = ["nombres"]
    def __str__(self):#return f"{self.nombres}"
        return 'id:{} usuario:{} empresa:{} sexo:{} nombres:{} apellidos:{} correo:{} cedula:{} num_telf:{} direccion:{} created_at:{} estatus:{} '.format(self.id,
        self.usuario,self.empresa,self.sexo,self.nombres,
        self.apellidos,self.correo,self.cedula,self.num_telf,
        self.direccion,self.created_at,self.estatus)