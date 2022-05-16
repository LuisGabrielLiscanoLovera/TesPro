from django.db import models
from authapp.models import MyUser as User
from empresa.models import Empresa
from operacion.models import Operacion
from talla.models import Talla
from patinador.models import Patinador




class Despacho(models.Model):
   

    usuario              = models.ForeignKey(User,related_name='Despacho', on_delete=models.CASCADE)
    patinador            = models.ForeignKey(Patinador, related_name='Despacho',  on_delete=models.CASCADE)
    empresa              = models.ForeignKey(Empresa, related_name='Despacho',  on_delete=models.CASCADE)
    operacion            = models.ForeignKey(Operacion,related_name='Despacho',on_delete=models.CASCADE)
    talla                = models.ForeignKey(Talla,related_name='Despacho',on_delete=models.DO_NOTHING)
    can_terminada        = models.IntegerField()
    nomTallaDespacho     = models.CharField(max_length=140)
    nomPatinadorDespacho = models.CharField(max_length=140)
    
    
    
    btnDelDespacho  = models.CharField(max_length=300, blank=True ,default="-" , null=True)
    #integrante = models.ForeignKey(Integrante,related_name='DespachoI', null=False, blank=False,on_delete=models.CASCADE)
    
    ESTATUS       = (('A','Activo'),('I','Inactivo'))
    estatus       = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'id:{} patinador:{}  can_termin:{} usuario:{} empresa:{} estatus:{}'.format(self.id,self.patinador, self.can_terminada,self.usuario,self.empresa,self.estatus)


class Task(models.Model):
    title = models.CharField(max_length=140)
    date  = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering=['completed','date']
        
        
        