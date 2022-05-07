from django.db import models
from authapp.models import MyUser as User
from empresa.models import Empresa
# Create your models here.

class Color(models.Model):
    usuario        = models.ForeignKey(User, related_name='Color', on_delete=models.CASCADE)
    empresa        = models.ForeignKey(Empresa, related_name='Color',on_delete=models.CASCADE)
    nom_color      = models.CharField(max_length=20)
    codigo_color   = models.CharField(blank=True, null=True,max_length=25)    
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at',]),
            
        ]
    def __str__(self):
            return '%s %s %i' % (self.id, self.nom_color, self.codigo_color)
  
 






