from django.db import models
from integrante.models import Integrante
from tarea.models import Tarea
from operacion.models import Operacion
# Create your models here.
from authapp.models import MyUser as User
class Destajo(models.Model):
    nom_operacion = models.ForeignKey(Operacion, related_name='Destajo',on_delete=models.CASCADE)
    tarea         = models.ForeignKey(Tarea, related_name='Destajo',on_delete=models.CASCADE)
    integrante    = models.ForeignKey(Integrante, related_name='Destajo',on_delete=models.CASCADE)
    cantidad      = models.IntegerField(blank=True, null=True)
    talla         = models.CharField(blank=True, null=True,max_length=5)
    usuario       = models.ForeignKey(User, null=True,blank=True,related_name='Destajo',on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.integrante)
    