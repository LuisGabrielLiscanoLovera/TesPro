from venv import create
from django.db import models
from authapp.models import MyUser as User
from empresa.models import Empresa
from integrante.models import Integrante
from talla.models import Talla
from patinador.models import Patinador
from tarea.models import Tarea
class Acumulado(models.Model):
    btnInfo       = '<button type="button" class="btn btn-outline-info text-center btn-sm btn-block ">Info</button>'
    btnAccion     = '<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>'
    usuario       = models.ForeignKey(User, on_delete=models.CASCADE)
    
    empresa       = models.ForeignKey(Empresa,  on_delete=models.CASCADE)
    nom_acumulado = models.CharField(max_length=35, unique=True)
    can_total     = models.IntegerField(blank=True, null=True,default=0)    
    nota          = models.CharField(max_length=50,blank=True, null=True)
    ESTATUS       = (('A','Activo'),('I','Inactivo'))
    estatus       = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    btnAcci       = models.CharField(max_length=300,default=btnAccion , null=True)
    delAcumulado  = models.CharField(max_length=150, default='' , null=True)
    btnInfo       = models.CharField(max_length=300,default=btnInfo , null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]

    def __str__(self):
        return 'id:{} usuario:{} empresa:{} nom_acumulado:{} created_at:{} estatus:{} '.format(
        self.id, self.usuario,self.empresa,
        self.nom_acumulado,self.created_at, self.estatus)



class ProAcumulado(models.Model):
    usuario       = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    acumulado     = models.ForeignKey(Acumulado, on_delete=models.CASCADE)
    integrante    = models.ForeignKey(Integrante, on_delete=models.CASCADE)
    talla         = models.ForeignKey(Talla,  on_delete=models.CASCADE,blank=True, null=True)
    patinador     = models.ForeignKey(Patinador, on_delete=models.CASCADE)
    tarea         = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    can_prod_acum = models.IntegerField()
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ['id']
        indexes = [models.Index(fields=['created_at',]),]
    def __str__(self):
        return 'id:{}  cantidad:{} created_at:{}'.format (self.id, self.can_prod_acum,self.created_at )