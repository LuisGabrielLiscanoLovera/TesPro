from django.db import models
from django import forms
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from empresa.models import Empresa
 

class MyUser(AbstractUser):
    empresa = models.ForeignKey(Empresa, null=True,related_name='MyUser',on_delete=models.CASCADE)
     #(queryset =Empresa.objects.all(), inicial = 0)
    logo = models.ImageField(upload_to='uploads/',null=True, height_field=None, width_field=None, max_length=100)
    logod = models.ImageField(upload_to='uploads/',null=True, height_field=None, width_field=None, max_length=100)
    
    