from django.db import models

# Create your models here.
#from django.contrib.auth.models import User
from authapp.models import MyUser as User
class Empresa(models.Model):    
    usuario       = models.ForeignKey(User,related_name='Empresa',on_delete=models.CASCADE)
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
        return '%s ' % (self.nom_empresa)

class RelacionEmpresa(models.Model):    
    usuario = models.ForeignKey(User, null=True,blank=True,related_name='RelacionEmpresa',on_delete=models.CASCADE)
    Empresa = models.ForeignKey(Empresa, null=True,blank=True,related_name='RelacionEmpresa',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
   
   
    class Meta:
        ordering = ["id"]
    def __str__(self):
        return '%s %s %s ' % (self.id, self.Empresa, self.usuario)
 

class CambioEmpres(models.Model):
    usuario = models.ForeignKey(User, related_name='CambioEmpres',on_delete=models.CASCADE)
    lastEm=models.IntegerField(default=+1)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
            ordering = ["id"]
    def __str__(self):
        return 'ID=%s lastEm=%s usuario=%s ' % (self.id, self.lastEm, self.usuario)
    
    
    
    """
    '''class MyModel(models.Model):
        title = models.CharField(max_length=120)
    text = models.TextField()
    auto_inc_and_filled = models.IntegerField()

    def save(self, *args, **kwargs):
        self.auto_inc_and_filled = MyModel.objects.count()
        super(MyModel, self).save(*args, **kwargs) '''
    """
    
    
