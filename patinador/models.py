from django.db import models
from empresa.models import Empresa
from integrante.models import Integrante
# Create your models here.

class Patinador(models.Model):
    
    empresa           = models.ForeignKey(Empresa, related_name='Patinador', null=False, blank=False,on_delete=models.CASCADE)
    nom_patinador      = models.OneToOneField(Integrante, related_name='Patinador', null=False, blank=False,on_delete=models.CASCADE)
    ESTATUS=(('A','Activo'),('I','Inactivo'))
    estutus       = models.CharField(max_length=1,choices=ESTATUS)
    password = models.CharField(max_length=100)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["nom_patinador"]
    def __str__(self):
        return str(self.nom_patinador)

 