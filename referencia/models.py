from django.db import models
from authapp.models import MyUser
from empresa.models import Empresa
# Create your models here.

class Referencia(models.Model):
    btnInfo         = '<button type="button" class="btn btn-outline-info text-center btn-sm btn-block ">Info</button>'
    btnAccion       = '<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>'
   
    usuario         = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    empresa         = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    nom_referencia  = models.CharField(max_length=30)
    descripcion     = models.CharField(max_length=150)
    
    
    #fotoPrendaUno = models.ImageField(upload_to='uploads/',null=False,blank=True ,height_field=None, width_field=None, max_length=100)
    #fotoPrendaDos = models.ImageField(upload_to='uploads/',null=False,blank=True ,height_field=None, width_field=None, max_length=100)
    ESTATUS         = (('A','Activo'),('I','Inactivo'))
    estatus         = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    btnAcci         = models.CharField(max_length=300, default=btnAccion, null=True)
    btnInfo         = models.CharField(max_length=300, default=btnInfo, null=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]
    def __str__(self):
        return 'id:{} nom_referencia:{} descripcion:{} usuario:{} empresa:{} created_at:{} estatus:{} ' .format (self.id,
        self.nom_referencia,
        self.descripcion,
        self.usuario,self.empresa,
        self.created_at,self.estatus)