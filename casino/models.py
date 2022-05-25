from django.db import models
from authapp.models import MyUser as User
from empresa.models import Empresa
from integrante.models import Integrante
from patinador.models import Patinador

class Casino (models.Model):
    btnInfo       = '<button type="button" class="btn btn-outline-info text-center btn-sm btn-block ">Info</button>'
    btnccion      = '<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>'
    usuario       = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa,  on_delete=models.CASCADE)
    nom_casino    = models.CharField(max_length=35, unique=True)
    can_total     = models.IntegerField(blank=True, null=True,default=0)
    ESTATUS       = (('A','Activo'),('I','Inactivo'))
    btnccion      = models.CharField(max_length=300,default=btnccion , null=True)
    btnInfo       = models.CharField(max_length=300,default=btnInfo , null=True)
    estatus       = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]
    def __str__(self):
        return 'id:{} usuario:{} empresa:{} nom_casino:{} can_total:{} estatus:{} created_at:{} '.format(
        self.id, self.usuario,self.empresa,
        self.nom_casino,self.can_total, self.estatus,self.created_at)

class Importe(models.Model):
    usuario         = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa         = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    casino          = models.ForeignKey(Casino, on_delete=models.CASCADE)
    cantidad        = models.IntegerField(blank=True, null=True)
    integrante      = models.ForeignKey(Integrante, on_delete=models.CASCADE)
    patinador       = models.ForeignKey(Patinador, on_delete=models.CASCADE)
    delCasinoImport = models.CharField(max_length=300, default='' , null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['created_at',]), 
        ]
    def __str__(self):
        return 'id:{} integrante:{} cantidad:{}   creatd_at:{}' .format(self.id,
        self.integrante,self.cantidad,self.created_at)
    
    