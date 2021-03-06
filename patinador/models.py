from django.db import models
from empresa.models import Empresa
from integrante.models import Integrante
from authapp.models import MyUser 
# Create your models here.

class Patinador(models.Model):
    usuario        = models.ForeignKey(MyUser, related_name='user',on_delete=models.CASCADE)
    empresa        = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    integrante     = models.OneToOneField(Integrante,on_delete=models.CASCADE)
    password       = models.CharField(max_length=100)
    created_at     = models.DateTimeField(auto_now_add=True)
    created_atv    = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    
    ctrlDespacho   = models.BooleanField(default=False)
    ctrlProduccion = models.BooleanField(default=False)
    ctrlCasino     = models.BooleanField(default=False) 
    btnAcci        = models.CharField(max_length=150, default='<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>' )
    ESTATUS        = (('A','Activo'),('I','Inactivo'))
    estatus        = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True) 
    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['created_at',]),            
        ]
    def __str__(self):
        return 'id:{} usuario:{} empresa:{} integrante:{} created_at:{} estatus:{} '.format (self.id, self.usuario,
        self.empresa,self.integrante,
        self.created_at,self.estatus,
        )