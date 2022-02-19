from django.db import models
from authapp.models import MyUser as User
from empresa.models import Empresa
# Create your models here.


class Tarea(models.Model):
    
    usuario       = models.ForeignKey(User, related_name='Tarea', null=True, blank=True,on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa, related_name='Tarea', null=False, blank=False,on_delete=models.CASCADE)
    
    nom_tarea     = models.CharField(max_length=20)
    min_minuto      = models.IntegerField(blank=True, null=True)
    min_hora      = models.IntegerField(blank=True, null=True)

    valor         = models.IntegerField(blank=True, null=True)
    detalle       = models.CharField(max_length=150)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    btnInfo = models.CharField(max_length=100, blank=True ,default='<button type="button" class="btn    btn-outline-info text-center btn-sm btn-block">Info</button>', null=True)
    btnAcci = models.CharField(max_length=100, blank=True ,default='<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>' , null=True)

    def __str__(self):
        return self.nom_tarea
