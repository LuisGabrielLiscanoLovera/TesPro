from django.db import models
from authapp.models import MyUser as User
from empresa.models import Empresa
from operacion.models import Operacion
# Create your models here.
# revisar la cuestion de modelo de tabla unica para nomretalla
class Talla(models.Model):
    usuario       = models.ForeignKey(User, related_name='Talla', on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa, related_name='Talla',on_delete=models.CASCADE)
    nom_talla     = models.CharField(max_length=10)
    num_talla     = models.IntegerField(blank=True, null=True) 
    
    btnAcci        = models.CharField(max_length=150, default='<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>' )
    btnAddTalla    = models.CharField(max_length=150, default='' , null=True)
    
    ESTATUS        = (('A','Activo'),('I','Inactivo'))
    estatus        = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]

    def __str__(self):
        return '%s %s %s %s %s %s ' % (self.id, self.usuario, self.empresa,self.nom_talla,self.num_talla,self.created_at)
    
class CanTalla(models.Model):
    usuario       = models.ForeignKey(User, related_name='CanTalla',on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa, related_name='CanTalla', on_delete=models.CASCADE)
    can_talla     = models.IntegerField(blank=True, null=True)
    res_talla     = models.IntegerField(blank=True, null=True)
    talla         = models.ForeignKey(Talla, related_name='CanTalla',on_delete  =models.CASCADE)
    operacion     = models.ForeignKey(Operacion, related_name='CanTalla',on_delete=models.CASCADE)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]

    def __str__(self):
        return 'id:{} usuario:{} empresa:{} can_talla:{} res_talla:{} talla_id:{} operacion:{} created_at:{}'.format(self.id, self.usuario, self.empresa,self.can_talla,self.res_talla,self.talla,self.operacion,self.created_at)

