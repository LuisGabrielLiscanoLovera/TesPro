from django.db import models
from authapp.models import MyUser 
#company
class Empresa(models.Model):    
    usuario = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    nom_empresa   = models.CharField(max_length=150,unique=True)
    direccion     = models.CharField(max_length=150)
    descripcion   = models.CharField(max_length=100)
    logo_empresa  = models.ImageField(upload_to='uploads/',null=True, height_field=None, width_field=None, max_length=100)
    ESTATUS    = (('A','Activo'),('I','Inactivo'))
    estatus    = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
   
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return '{}'.format(self.nom_empresa)

#business relationship
class RelacionEmpresa(models.Model):    
    usuario = models.ForeignKey(
        MyUser, null=True, blank=True, on_delete=models.CASCADE)
    Empresa = models.ForeignKey(Empresa, null=True,blank=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
   
   
    class Meta:
        ordering = ["id"]
    def __str__(self):
        return 'id:{} empresa:{} usuario:{} '.format (self.id, self.Empresa, self.usuario)
 
#company change 
class CambioEmpres(models.Model):
    usuario = models.ForeignKey(
        MyUser, null=True, blank=True, on_delete=models.CASCADE)
    lastEm       = models.IntegerField(default=+1)
    created_at   = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["id"]
    def __str__(self):
        return 'id:{} lastEm:{} usuario:{} '.format (self.id, self.lastEm, self.usuario)
