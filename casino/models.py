from django.db import models
from authapp.models import MyUser as User
from empresa.models import Empresa
from integrante.models import Integrante
# Create your models here.
class Casino(models.Model):
    
    
    btnInfoStrin='<button type="button" class="btn btn-outline-info icofont-info-squar text-center btn-md btn-block">Info</button>'
    
    formCasino ='<button type="button" class="btn btn-outline-warning icofont-settings-al text-center btn-md btn-block ">Accion</button>'
    
    
    usuario    = models.ForeignKey(User, related_name='Casino',on_delete = models.CASCADE)
    empresa    = models.ForeignKey(Empresa, related_name='Casino',on_delete = models.CASCADE)
    integrante = models.OneToOneField(Integrante, related_name='Casino',on_delete= models.CASCADE)
    
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
    
    
class Importe(models.Model):
    empresa    = models.ForeignKey(Empresa, related_name='Importe', null=False, blank=False,on_delete=models.CASCADE)
    casino     = models.ForeignKey(Casino, related_name='Importe', null=False, blank=False,on_delete=models.CASCADE)
    cantidad   = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]
    def __str__(self):
        return '%s %s %s' % (self.id, self.cantidad,self.created_at)
    
    