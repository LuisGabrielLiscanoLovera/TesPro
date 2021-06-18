from django.db import models
from empresa.models import Empresa
from integrante.models import Integrante
from authapp.models import MyUser as User

# Create your models here.

class Patinador(models.Model):
    usuario        = models.ForeignKey(User, related_name='Patinador', null=True, blank=True,on_delete=models.CASCADE)

    empresa           = models.ForeignKey(Empresa, related_name='Patinador', null=False, blank=False,on_delete=models.CASCADE)
    nom_patinador      = models.OneToOneField(Integrante, related_name='Patinador', null=False, blank=False,on_delete=models.CASCADE)
    ESTATUS=(('A','Activo'),('I','Inactivo'))
    estatus        = models.CharField(max_length=1,choices=ESTATUS)
    password       = models.CharField(max_length=100)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.id, self.usuario, self.empresa,self.nom_patinador,self.usuario,self.estatus,self.created_at)
 