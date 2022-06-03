from django.db import models
from empresa.models import Empresa
from authapp.models import MyUser as User
from operacion.models import Operacion
from talla.models import Talla
from tarea.models import Tarea
from integrante.models import Integrante
from patinador.models import Patinador
class Produccion(models.Model):
    usuario       = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa,   on_delete=models.CASCADE)
    operacion     = models.ForeignKey(Operacion,on_delete=models.CASCADE)
    tarea         = models.ForeignKey(Tarea,on_delete=models.DO_NOTHING,blank=True, null=True)
    talla         = models.ForeignKey(Talla,related_name='ProduccionTallaFK',on_delete=models.DO_NOTHING, blank=True, null=True)
    can_terminada = models.IntegerField()
    integrante    = models.ForeignKey(Integrante,related_name='ProduccionI',on_delete=models.CASCADE)
    patinador     = models.ForeignKey(Patinador,  blank=True, null=True, on_delete=models.CASCADE)
    delProduccion = models.CharField(max_length=200, default='' , null=True)
    ESTATUS       = (('A','Activo'),('I','Inactivo'))
    estatus       = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    fecha_cierre  = models.DateTimeField(blank=True,null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'id:{}, usuario:{}, empresa:{}, operacion:{},tarea:{}, talla:{}, can_terminada:{}, integrante:{}, patinador:{}, costeProd:{} fecha:{}'.format(self.id, self.usuario, self.empresa, self.operacion, self.tarea, self.talla, self.can_terminada, self.integrante, self.patinador,self.costeProd, self.created_at)

