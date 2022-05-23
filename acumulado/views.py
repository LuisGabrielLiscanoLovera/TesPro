from django import views
import json
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from integrante.models import Integrante
from patinador.models import Patinador
from talla.models import Talla,CanTalla
from operacion.models import Operacion 
from django.db.models import Sum, F 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authapp.models import MyUser
from acumulado.models import Acumulado as ACU
from acumulado.models import ProAcumulado as  ProAcu
from django.views.generic import View
from django.http import JsonResponse, Http404, HttpResponse
from django.db.models import F
from acumulado.serializers import AcumuladoSerializer

class Acumulado(TemplateView):
     
     template_name = "pages/acumulado.html"
     success_url = '/'
     
     def get_context_data(self, **kwargs):
          context = super(Acumulado, self).get_context_data(**kwargs)
          s = SessionStore()
          s['last_login'] = self.request.user.pk
          s.create()      
          
          AllEmpresa      = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])       
          lastEm          = CambioEmpres.objects.filter(usuario_id=s['last_login']).last()
          Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('id','nom_talla','num_talla')
          EmpresaActual   = Empresa.objects.filter(usuario=s['last_login'],id=int(lastEm.lastEm))
          Operaciones     = Operacion.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),estatus='A').values('nom_operacion','id')
          context = super(Acumulado, self).get_context_data(**kwargs)
          context['lastIdEmpresa']    = int(lastEm.lastEm) #ids empresas
          context['allTalla']         = Tallas             #todaslas las tallas
          context['allOperaciones']   = Operaciones        #todaslas operaciones 
          context['nomEmpresa']       = AllEmpresa         #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual      # nombre de la empresa actual
          context['last_login']       = s['last_login']    # ultimo inicio de seccion   
          try:
            patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('integrante_id')
            allPatinadores  = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),id=int(patinadores[0].get('integrante_id'))).values('nombres','apellidos','id')
            context['allPatinador']     = allPatinadores     #todos los patinadores de la empresa
            return context
          
          finally:
            return context
       
          
          
@api_view(['GET'])  
def AcomuladoList(request):
    if request.session.has_key('username'):
            if 'username' in request.session:
                username = request.session['username']
                idUser   = MyUser.objects.get(username = username)
    
    lastEm          = CambioEmpres.objects.filter(usuario_id = idUser.id).last()
    acumuladoQsect  = ACU.objects.filter(empresa_id = lastEm.lastEm).order_by('-id')
    AcomuladoSe     = AcumuladoSerializer(acumuladoQsect, many=True)   
    dump            = json.dumps(AcomuladoSe.data)   #dump serializer to json reponse 
    return HttpResponse(dump, content_type='application/json')
    
    

@api_view(['POST'])
def createAcumulado(request,):
    #Prod = Models AcumulcreateAcumulado
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
        
    lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last()  
    canTerminada  = int(request.data['can_total_acu'])
    
    try: 
        obj = ACU.objects.create(
        usuario_id     = int(idUser.id),
        empresa_id     = int(lastEm.lastEm),
        nom_acumulado  = request.data['nom_acumulado'],
        nota           = request.data['nota_acu'],
        can_total      = canTerminada,      
        )
                
        #obj = ACU.objects.latest('id')
        #btnDel="<button class='btn btn-block btn-sm btn-outline-danger icofont-ui-remove' type='submit' onclick='deleteProduccionUnico({})'> </button>".format(obj.id)
        #obj = ACU.objects.all().filter(id=obj.id).update(delAcumulado=btnDel)
        data = {            'Acumulado': "Acumulado guardado con exito!",
            'estatus':True
        }

    except Exception as e:
        data = { 'Acumulado': str(e),'estatus':False}        
        return Response("Acumulado no cargadA " +str(e) )
    return Response(data)
    
    



@api_view(['POST'])
def createProAcumulado(request,):

    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
        
    lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last()  
    canTerminada  = int(request.data['Cantidad_Acu'])
    print(int(request.data['OccionId_pantinador_Acu']),"gggggggggg")    
    
    try: 
        obj = ProAcu.objects.create(
        usuario_id     = int(idUser.id),
        empresa_id     = int(lastEm.lastEm),
        integrante_id  = int(request.data['OccionId_integrante_Acu']),
        patinador_id   = int(request.data['OccionId_pantinador_Acu']),
        tarea_id       = int(request.data['OccionId_tarea_Acu']),
        talla_id       = int(request.data['OccionId_talla_Acu']),
        can_prod_acum  = canTerminada,      
        acumulado_id    =int(request.data['acumulado_id'])
        )
                
        #obj = ACU.objects.latest('id')
        #btnDel="<button class='btn btn-block btn-sm btn-outline-danger icofont-ui-remove' type='submit' onclick='deleteProduccionUnico({})'> </button>".format(obj.id)
        #obj = ACU.objects.all().filter(id=obj.id).update(delAcumulado=btnDel)
        data = {
            'Acumulado': "Acumulado guardado con exito!",
            'estatus':True
        }
       
      

    except Exception as e:
        data = {'Acumulado': str(e),'estatus':False}        
        return Response(data)
    
    return Response(data)
    
    