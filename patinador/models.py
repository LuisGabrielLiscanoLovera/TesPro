from django.db import models
from empresa.models import Empresa
from integrante.models import Integrante
from authapp.models import MyUser as User

# Create your models here.

class Patinador(models.Model):
    usuario        = models.ForeignKey(User, related_name='Patinador', null=True, blank=True,on_delete=models.CASCADE)
    empresa        = models.ForeignKey(Empresa, related_name='Patinador', null=False, blank=False,on_delete=models.CASCADE)
    integrante     = models.OneToOneField(Integrante, related_name='Patinador', null=False, blank=False,on_delete=models.CASCADE)
    ESTATUS        = (('A','Activo'),('I','Inactivo'))
    estatus        = models.CharField(max_length=1,choices=ESTATUS)
    password       = models.CharField(max_length=100)
    created_at     = models.DateTimeField(auto_now_add=True)
    created_atv    = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    
    
    btnAcci = models.CharField(max_length=97, blank=True ,default='<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>' , null=True)
    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.id, self.usuario, self.empresa,self.integrante,self.usuario,self.estatus,self.created_at)