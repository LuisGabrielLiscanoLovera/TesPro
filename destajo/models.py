from django.db import models
from integrante.models import Integrante
from tarea.models import Tarea
from prenda.models import Prenda
# Create your models here.
from django.contrib.auth.models import User
class Destajo(models.Model):
    nom_operacion = models.ForeignKey(Prenda, related_name='Destajo',on_delete=models.CASCADE)
    tarea         = models.ForeignKey(Tarea, related_name='Destajo',on_delete=models.CASCADE)
    integrante    = models.ForeignKey(Integrante, related_name='Destajo',on_delete=models.CASCADE)
    cantidad      = models.IntegerField(blank=True, null=True)
    talla         = models.CharField(blank=True, null=True,max_length=5)
    can_resta     = models.IntegerField(blank=True, null=True)
    # user = models.ForeignKey(User, related_name='destajo',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #user      = models.ForeignKey(User, related_name='Destajo', null=False, blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.integrante)
    