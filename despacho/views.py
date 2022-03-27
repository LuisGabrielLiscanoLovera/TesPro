# Create your views here
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from despacho.models import Despacho
from integrante.models import Integrante
from patinador.models import Patinador
from talla.models import Talla
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authapp.models import MyUser
from .serializers import DespachoSerializer,OperacionSerializer
from patinador.serializers import PatinadorSerializer
from operacion.models import Operacion
from django.views.generic import View
from django.http import JsonResponse, Http404, HttpResponse
from .models import Task
from .forms import TaskForms
from django.forms.models import model_to_dict

#original

@api_view(['GET'])
def despacho_list(request):
    if request.session.has_key('username'):
         #capturamos el inicio de session 
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
    
    lastEm     = CambioEmpres.objects.filter(Usuario_id=idUser).last()
    lastEm = lastEm
    despachos = Operacion.objects.filter(empresa_id=lastEm,estatus='A').order_by('-id')
    despachos = Despacho.objects.all();   
    tSerializer = DespachoSerializer(despachos, many = True)
    #return JsonResponse(tSerializer.data, safe=False)
    return Response(tSerializer.data)
    
#


@api_view(['GET'])
def get_despacho(request, id):
    

    try: 
        despacho = Despacho.objects.get(id = id)
    except Exception as e:
        raise Http404
    tSerializer = DespachoSerializer(despacho)
    return Response(tSerializer.data)

@api_view(['DELETE'])
def deleteDespacho(request, id):
    despacho = Despacho.objects.get(id = id)
    try:
        despacho.delete()
    except Exception as e:
        Response("Unable to Delete Task!")
    return Response("Task Deleted Sucessfully")




@api_view(['GET'])  
def operacionesList(request):
     
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    lastEm     = CambioEmpres.objects.filter(Usuario_id=idUser).last()
    lastEm=lastEm.lastEm
    
    despacho  = Operacion.objects.filter(empresa_id=lastEm,estatus='A').order_by('-id')
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
     
     template_name = "despacho/despacho.html"
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
    
    print(request.data['id_OP'])
    print(request.data)
    
    print("empresa=",lastEm.lastEm,
    "iduser=",idUser.id,
    "idop=",request.data['id_OP'],
    "idtalla=",request.data['selectIdTalla'],
    "idpatinador=",request.data['selectIDPatinador'],
    "cantidad=",int(request.data['cant']) )
        
    obj = Despacho.objects.create(
        usuario_id     = int(idUser.id),
        patinador_id   = int(request.data['selectIDPatinador']),
        empresa_id     = int(lastEm.lastEm),
        operacion_id   = int(request.data['id_OP']), 
        talla_id       = int(request.data['selectIdTalla']),
        can_terminada  = int(request.data['cant'])
          
              
        )
    
    data = {
        'user': "user"
    } 
    return JsonResponse(data)