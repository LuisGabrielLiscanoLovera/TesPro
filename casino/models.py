from django.db import models
from integrante.models import Integrante
from authapp.models import MyUser as User
from empresa.models import Empresa
# Create your models here.
class Casino(models.Model):
    usuario    = models.ForeignKey(User, related_name='Casino', null=False, blank=True,on_delete  = models.CASCADE)
    empresa    = models.ForeignKey(Empresa, related_name='Casino', null=False, blank=False,on_delete=models.CASCADE)
    integrante = models.ForeignKey(Integrante, related_name='Casino', null=False, blank=False,on_delete=models.CASCADE)
    cantidad   = models.IntegerField(blank=True, null=True)
    deuda      = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    btnInfo = models.CharField(max_length=100, blank=True ,default='<button type="button" class="btn btn-outline-light text-center btn-sm btn-block">Info</button>', null=True)
    btnAcci = models.CharField(max_length=100, blank=True ,default='<button type="button" class="btn btn-outline-light text-center btn-sm btn-block ">Accion</button>' , null=True)
    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.id, self.usuario, self.empresa,self.integrante,self.deuda,self.estatus,self.created_at)