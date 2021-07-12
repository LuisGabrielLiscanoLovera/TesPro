from django.db import models
from authapp.models import MyUser as User
from empresa.models import Empresa
from integrante.models import Integrante
# Create your models here.
class Casino(models.Model):
    btnInfoStrin='<button type="button" class="btn btn-outline-info icofont-info-square text-center btn-sm btn-block"></button>'
    
    formCasino ='<button type="button" class="btn btn-outline-light text-center btn-sm btn-block ">Accion</button>'
    
    
    usuario    = models.ForeignKey(User, related_name='Casino', null=False, blank=True,on_delete  = models.CASCADE)
    empresa    = models.ForeignKey(Empresa, related_name='Casino', null=False, blank=False,on_delete=models.CASCADE)
    integrante = models.OneToOneField(Integrante, related_name='Casino', null=False, blank=False,on_delete=models.CASCADE)
    cantidad   = models.IntegerField(blank=True, null=True)
    deuda      = models.IntegerField(blank=True, null=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    btnInfo = models.CharField(max_length=1000, blank=True ,default=btnInfoStrin, null=True)
    btnAcci = models.CharField(max_length=1000, blank=True ,default=formCasino , null=True)
    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]
    def __str__(self):
        return '%s %s %s %s %s' % (self.id, self.usuario, self.empresa,self.deuda,self.created_at)