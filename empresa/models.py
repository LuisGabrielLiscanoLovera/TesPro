from django.db import models

# Create your models here.


class Empresa(models.Model):
    nom_empresa = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ["nom_empresa"]

    def __str__(self):
        return self.nom_empresa

