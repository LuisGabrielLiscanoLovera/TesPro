from django.db import models

# Create your models here.
class Tarea(models.Model):
    nom_tarea     = models.CharField(max_length=20)
    duracion      = models.IntegerField(blank=True, null=True)
    valor         = models.IntegerField(blank=True, null=True)
    min_hora      = models.IntegerField(blank=True, null=True)
    detalle       = models.CharField(max_length=150)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom_tarea
