from django.db import models
from empresa.models import Empresa
from authapp.models import MyUser as User
from operacion.models import Operacion
from talla.models import Talla
from tarea.models import Tarea
from integrante.models import Integrante
from patinador.models import Patinador



class Produccion(models.Model):
    usuario              = models.ForeignKey(User,related_name='Produccion', on_delete=models.CASCADE)
    empresa              = models.ForeignKey(Empresa, related_name='Produccion',  on_delete=models.CASCADE)
    operacion            = models.ForeignKey(Operacion,related_name='Produccion',on_delete=models.CASCADE)
    tarea                = models.ForeignKey(Tarea,related_name='Produccion',on_delete=models.DO_NOTHING,blank=True, null=True)
    talla                = models.ForeignKey(Talla,related_name='Produccion',on_delete=models.DO_NOTHING, blank=True, null=True)
    can_terminada        = models.IntegerField()
    integrante           = models.ForeignKey(Integrante,related_name='ProduccionI',on_delete=models.CASCADE)
    patinador            = models.ForeignKey(Patinador, related_name='Produccion',  on_delete=models.CASCADE)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        #       return 'id:{}'.format(self.id)
        return  'id:{}, usuario:{}, empresa:{}, operacion:{},tarea:{}, talla:{}, can_terminada:{}, integrante:{}, patinador:{}, fecha:{}'.format(self.id,self.usuario,self.empresa, self.operacion,self.tarea,self.talla,self.can_terminada,self.integrante,self.patinador,self.created_at)

