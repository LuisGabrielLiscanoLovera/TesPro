# Create your views here
from django import views
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from despacho.models import Despacho
from integrante.models import Integrante
from patinador.models import Patinador
from talla.models import Talla,CanTalla
from django.db.models import Sum, F 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authapp.models import MyUser
from .serializers import DespachoSerializer,OperacionSerializer
from patinador.serializers import PatinadorSerializer
from operacion.models import Operacion
from django.views.generic import View
from django.http import JsonResponse, Http404, HttpResponse


























from pprint import pprint


from django.db.models import F

from django_serverside_datatable.views import ServerSideDatatableView

class ItemListView(ServerSideDatatableView):   
    
    #columns = ['id', 'can_terminada','created_at','patinador_id','empresa','talla','nomPatinadorDespacho','nomTallaDespacho']    

    
    columns = ['nomPatinadorDespacho','nomTallaDespacho','can_terminada','created_at','id']
    
    def get_queryset(self):
        if self.request.method == 'GET':           
            idOp = self.request.GET.get('idOp', None)
            idUser = self.request.GET.get('usuario', None)            
            
            if idOp and idUser is not None:
                lastEm     = CambioEmpres.objects.filter(Usuario_id=idUser).last()      
                queryset   = Despacho.objects.filter(empresa_id=lastEm.lastEm,operacion_id=idOp).order_by('-id') #.select_related('patinador')#.filter(type=Integrante.objects.get(id=))               
                
                
            return queryset
    
    




        









#original
@api_view(['GET'])
def despacho_list(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    #crear registro de despacho
    idOp       = request.GET.get('idOp', None)
    lastEm     = CambioEmpres.objects.filter(Usuario_id=idUser).last()   
    despachos  = Despacho.objects.all().filter(empresa_id=lastEm.lastEm,operacion_id=idOp).order_by('-id')
    
    tSerializer = DespachoSerializer(despachos, many = True)
    
    return JsonResponse(tSerializer.data, safe=False)
    #return Response(tSerializer.data)
    
#

@api_view(['DELETE'])
def deleteDespacho(request,id):

    id_despacho = request.GET.get('id', None)

    try:
        id= request.GET.get('id_despacho', None)
      
        r=Despacho.objects.all().filter(id=id)
       
        r.delete()
        
        
        
        
        '''  canTerminada =  Despacho.objects.filter(id=id).values('can_terminada','operacion_id')
        for event in canTerminada:
            canTerminada=(event['can_terminada'])
            operacion_id=(event['operacion_id'])
        CanTalla.objects.all().filter(operacion_id=operacion_id).update(res_talla= F('res_talla') + canTerminada)
        Operacion.objects.all().filter(id=operacion_id).update(can_restante= F('can_restante') + canTerminada)
        Despacho.objects.get(id=id).delete() '''
        
        data = {
            'deleted': True
        }
        
    except Exception as e:
        print(str(e))
        
        data = {
            'deleted': False
            
        }
        
        Response("Unable to Delete Task!")
    return JsonResponse(data)
    #return Response("Task Deleted Sucessfully")
        
    
    
    
    
    






@api_view(['GET'])  
def operacionesList(request):
     
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    lastEm     = CambioEmpres.objects.filter(Usuario_id=idUser).last()   
    despacho  = Operacion.objects.filter(empresa_id=lastEm.lastEm,estatus='A').order_by('-id')
    serializer = OperacionSerializer(despacho, many=True)
   
    return Response(serializer.data)



@api_view(['GET'])  
def patinadoresAct(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    lastEm = CambioEmpres.objects.filter(Usuario_id=idUser).last()
    lastEm = lastEm.lastEm    
    try:        
        patinadores     = Patinador.objects.all().filter(usuario=idUser,estatus='A',empresa_id=int(lastEm))
        serializer      = PatinadorSerializer(patinadores, many=True)
        return Response(serializer.data)
    except Exception as e:    
        print("no tienes patinadores activos")  
    
        return Response("no tienes patinadores activos")
        

class Despachos(TemplateView):
     
     template_name = "pages/despacho.html"
     success_url = '/'
     
     def get_context_data(self, **kwargs):
          s = SessionStore()
          s['last_login'] = self.request.user.pk
          s.create()
          AllEmpresa      = RelacionEmpresa.objects.filter(Usuario_id=s['last_login'])       
          lastEm          = CambioEmpres.objects.filter(Usuario_id=s['last_login']).last()

          Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('id','nom_talla','num_talla')
          EmpresaActual   = Empresa.objects.filter(usuario=s['last_login'],id=int(lastEm.lastEm))
          Operaciones     = Operacion.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),estatus='A').values('nom_operacion','id')
          patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('integrante_id')
          allPatinadores  = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),id=int(patinadores[0].get('integrante_id'))).values('nombres','apellidos','id')
          
          
          context = super(Despachos, self).get_context_data(**kwargs)
          
          context['lastIdEmpresa']    = int(lastEm.lastEm) # ids empresas
          context['allTalla']         = Tallas             #todaslas las tallas
          context['allOperaciones']   = Operaciones        #todaslas operaciones 
          context['allPatinador']     = allPatinadores     #todos los patinadores de la empresa
          context['nomEmpresa']       = AllEmpresa         #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual      # nombre de la empresa actual
          context['last_login']       = s['last_login']    # ultimo inicio de seccion

          
          
          
          return context



@api_view(['POST'])
def createDespacho(request,):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
        
    lastEm           = CambioEmpres.objects.filter(Usuario_id=idUser.id).last()
    #serializer = DespachoSerializer(data = request.data)
    
    #print(request.data['id_OP'])
    #print(request.data)
    
    
    canTerminada  = int(request.data['cant'])
    nombreTalla   = Talla.objects.filter(id=int(request.data['selectIdTalla'])).values('nom_talla')
    nomPatinador  = Integrante.objects.filter(id=int(request.data['selectIDPatinador'])).values('nombres','apellidos')
    nom_patinador = nomPatinador[0]['nombres']+" "+nomPatinador[0]['apellidos']
    
    try:
        
        
        obj = Despacho.objects.create(
        usuario_id           = int(idUser.id),
        patinador_id         = int(request.data['selectIDPatinador']),
        empresa_id           = int(lastEm.lastEm),
        operacion_id         = int(request.data['id_OP']), 
        talla_id             = int(request.data['selectIdTalla']),
        can_terminada        = canTerminada,
        nomTallaDespacho     = nombreTalla[0]['nom_talla'],
        nomPatinadorDespacho = nom_patinador

        )      
        data = {
            'despacho': True
        }
        
        
        CanTallaOP      = CanTalla.objects.all().filter(talla_id=int(request.data['selectIdTalla'])).update(res_talla= F('res_talla') - canTerminada)
        OpTallaRestante = Operacion.objects.all().filter(id=int(request.data['id_OP'])).update(can_restante= F('can_restante') - canTerminada)
        
        
        
        
        return Response(data)
    except Exception as e:
        print(str(e))
        return Response("despacho no cargado")
 
   
