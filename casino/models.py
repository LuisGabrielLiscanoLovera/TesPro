from django.db import models
from integrante.models import Integrante
#from empresa.models import Empresa


# Create your models here.
class Casino(models.Model):
   
    integrante = models.ForeignKey(Integrante, null=False, blank=False,on_delete=models.CASCADE)
    cantidad   = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return str(self.integrante)