from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Empresa(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    nom_empresa = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ["nom_empresa"]

    def __str__(self):
        return self.nom_empresa

