# Create your views here
import json
from textwrap import indent
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.contrib.sessions.backends.db import SessionStore
from rest_framework.response import Response
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from talla.models import Talla
from operacion.models import Operacion
from patinador.models import Patinador
from integrante.models import Integrante
from produccion.models import Produccion as Prod
from authapp.models import MyUser
from .serializers import ProduccionSerializer
from rest_framework.decorators import api_view

from django.http import HttpResponse
class Produccion(TemplateView):
     template_name = "pages/produccion.html"     
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
          
          
          context = super(Produccion, self).get_context_data(**kwargs)
          
          context['lastIdEmpresa']    = int(lastEm.lastEm) # ids empresas
          context['allTalla']         = Tallas             #todaslas las tallas
          context['allOperaciones']   = Operaciones        #todaslas operaciones 
          context['allPatinador']     = allPatinadores     #todos los patinadores de la empresa
          context['nomEmpresa']       = AllEmpresa         #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual      # nombre de la empresa actual
          context['last_login']       = s['last_login']    # ultimo inicio de seccion

          
          
          
          return context


@api_view(['GET'])  
def ProduccionOPList(request):
    if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username = username)
                 
    lastEm     = CambioEmpres.objects.filter(Usuario_id = idUser.id).last() 
    produccion = Prod.objects.filter(empresa_id = lastEm.lastEm,operacion_id=int(request.GET.get('idOp', None))).order_by('-id')
    ProduccionSe = ProduccionSerializer(produccion, many=True)   
    dump = json.dumps(ProduccionSe.data)   #dump serializer to json reponse 
    
    
    return HttpResponse(dump, content_type='application/json')
    




@api_view(['POST'])
def createProduccion(request,):
    #Prod = Models Produccion
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
        
    lastEm           = CambioEmpres.objects.filter(Usuario_id=idUser.id).last()  
    
    canTerminada  = int(request.data['cantidadProd'])
    try: 
        obj = Prod.objects.create(
        usuario_id           = int(idUser.id),
        patinador_id         = int(request.data['OccionId_pantinador_prod']),
        integrante_id        = int(request.data['OccionId_integrante_prod']),
        empresa_id           = int(lastEm.lastEm),
        operacion_id         = int(request.data['idOperacion']),
        talla_id             = int(request.data['OccionId_talla']),
        tarea_id             = int(request.data['OccionId_tarea']),
        can_terminada        = canTerminada       
        )
        obj = Prod.objects.latest('id')
        btnDel="<button class='btn btn-block btn-sm btn-outline-danger icofont-ui-remove' type='submit' onclick='deleteProduccionUnico({})'> </button>".format(obj.id)
        obj = Prod.objects.all().filter(id=obj.id).update(delProduccion=btnDel)
        data = {
            'produccion': "Produccion guardado con exito!",
            'estatus':True
        }
       
        return Response(data)

    except Exception as e:
        print(str(e))
        return Response("despacho no cargado " +str(e) )
 
   
   

   
    return HttpResponse()



@api_view(['DELETE'])
def deleteProduccion(request,id):
    try:      
        Prod.objects.get(id=id).delete()
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
    
        
    