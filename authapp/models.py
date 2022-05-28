from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
        #empresa = models.ForeignKey(Empresa, null=True,blank=True,related_name='MyUser',on_delete=models.CASCADE)
     #(queryset =Empresa.objects.all(), inicial = 0)
    patinador   = models.BooleanField(default=False,null=True,blank=True)
    #logo = models.ImageField(upload_to='uploads/',null=True, height_field=None, width_field=None, max_length=100)
    foto        = models.ImageField(upload_to='uploads/',null=False,blank=True ,height_field=None, width_field=None, max_length=100)    