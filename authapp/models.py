from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    integrante_id = models.IntegerField(blank=True, null=True)
    patinador = models.BooleanField(default=False, null=True, blank=True)
    #logo = models.ImageField(upload_to='uploads/',null=True, height_field=None, width_field=None, max_length=100)
    foto = models.ImageField(upload_to='uploads/', null=False,
                             blank=True, height_field=None, width_field=None, max_length=100)
