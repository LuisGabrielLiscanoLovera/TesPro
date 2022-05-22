from django import views
import json
from django.contrib.sessions.backends.db import SessionStore
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
from django.views.generic import View
from django.http import JsonResponse, Http404, HttpResponse
from django.db.models import F
from acumulado.serializers import AcumuladoSerializer

class Acumulado(TemplateView):
     
     template_name = "pages/acumulado.html"
     success_url = '/'
     
     def get_context_data(self, **kwargs):
          s = SessionStore()
          s['last_login'] = self.request.user.pk
          s.create()
          AllEmpresa      = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])       
          lastEm          = CambioEmpres.objects.filter(usuario_id=s['last_login']).last()
          Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('id','nom_talla','num_talla')
          EmpresaActual   = Empresa.objects.filter(usuario=s['last_login'],id=int(lastEm.lastEm))
          Operaciones     = Operacion.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),estatus='A').values('nom_operacion','id')
          patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('integrante_id')
          allPatinadores  = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),id=int(patinadores[0].get('integrante_id'))).values('nombres','apellidos','id')
          
          
          context = super(Acumulado, self).get_context_data(**kwargs)
          
          context['lastIdEmpresa']    = int(lastEm.lastEm) #ids empresas
          context['allTalla']         = Tallas             #todaslas las tallas
          context['allOperaciones']   = Operaciones        #todaslas operaciones 
          context['allPatinador']     = allPatinadores     #todos los patinadores de la empresa
          context['nomEmpresa']       = AllEmpresa         #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual      # nombre de la empresa actual
          context['last_login']       = s['last_login']    # ultimo inicio de seccion

          
          
          
          return context
          
          
@api_view(['GET'])  
def ProdAcomuladoList(request):
    if request.session.has_key('username'):
            if 'username' in request.session:
                username = request.session['username']
                idUser   = MyUser.objects.get(username = username)
    
    lastEm          = CambioEmpres.objects.filter(usuario_id = idUser.id).last()
    acumuladoQsect  = ACU.objects.filter(empresa_id = lastEm.lastEm).order_by('-id')
    AcomuladoSe = AcumuladoSerializer(acumuladoQsect, many=True)   
    dump = json.dumps(AcomuladoSe.data)   #dump serializer to json reponse 

    return HttpResponse(dump, content_type='application/json')
    