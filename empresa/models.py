from django.db import models

# Create your models here.
#from django.contrib.auth.models import User
from authapp.models import MyUser as User
class Empresa(models.Model):    
    #user = models.ForeignKey(User, null=True,blank=True,related_name='Empresa',on_delete=models.CASCADE)
    nom_empresa = models.CharField(max_length=30)
    direccion = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=100)
    logo_empresa = models.ImageField(upload_to='uploads/',null=True, height_field=None, width_field=None, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ["nom_empresa"]

    def __str__(self):
        return self.nom_empresa

class RelacionEmpresa(models.Model):    
    Usuario = models.ForeignKey(User, null=True,blank=True,related_name='RelacionEmpresa',on_delete=models.CASCADE)
    Empresa = models.ForeignKey(Empresa, null=True,blank=True,related_name='RelacionEmpresa',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.Empresa)

class CambioEmpres(models.Model):
    Usuario = models.ForeignKey(User, null=True,blank=True,related_name='CambioEmpres',on_delete=models.CASCADE)
    lastEm=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    