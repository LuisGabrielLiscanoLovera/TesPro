from django.db import models
from authapp.models import MyUser 
from empresa.models import Empresa


class Tarea(models.Model):
    
    usuario       = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    empresa       = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    #codigo_tarea  = models.CharField(blank=True, null=True,max_length=25)  
    nom_tarea     = models.CharField(max_length=50)
    min_minuto    = models.IntegerField(blank=True, null=True )
    min_hora      = models.IntegerField(blank=True, null=True )
    valor         = models.IntegerField(blank=True, null=True )    
    detalle       = models.CharField(blank=True, null=True,max_length=150 )
    btnInfo = models.CharField(max_length=100, default='<button type="button" class="btn    btn-outline-info text-center btn-sm btn-block">Info</button>')
    btnAcci = models.CharField(max_length=100, default='<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>')
    
    ESTATUS       = (('A','Activo'),('I','Inactivo'))
    estatus       = models.CharField(max_length=1,choices=ESTATUS,default='A',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    def __str__(self):
        return 'id:{} nomTarea:{} min_minuto:{} min_hora:{} valor:{} detalle:{} usuario:{} empresa:{} created_at:{} estatus:{}'.format(self.id,
        self.nom_tarea, self.min_minuto,
        self.min_hora,self.valor,
        self.detalle,self.usuario,
        self.empresa,
        self.created_at,self.estatus)
