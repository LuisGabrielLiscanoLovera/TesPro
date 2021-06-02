from django.db import models
from django.contrib.auth.models import User
from empresa.models import Empresa
# Create your models here.

class Color(models.Model):
    
    empresa           = models.ForeignKey(Empresa, related_name='Color', null=False, blank=False,on_delete=models.CASCADE)
    nom_color      = models.CharField(max_length=20, unique=True)
    codigo_color   = models.IntegerField()    
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["nom_color"]
    def __str__(self):
        return self.nom_color


# Create your models here.
class Todo(models.Model):
    # id is auto generated primary key
    item = models.CharField(max_length=60)
    itemd = models.CharField(max_length=60)
   
    def __str__(self):
        return self.itemd