from django.db import models
from django.contrib.auth.models import User

# Create your models here.

user      = models.ForeignKey(User, related_name='Integrante', null=False, blank=False,on_delete=models.CASCADE)