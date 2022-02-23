# Create your views here
from django.contrib.sessions.backends.db import SessionStore
from django.views.generic.base import TemplateView
from django.views.generic.base import TemplateView as TVB
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from integrante.models import Integrante
from patinador.models import Patinador
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authapp.models import MyUser
from .serializers import DespachoSerializer
from operacion.models import Operacion
from django.views.generic import View
from django.http import JsonResponse

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/despacho-list/'
		}
	return Response(api_urls)
#@login_required(login_url='signin')


@api_view(['GET'])  
def despachoList(request):
    #capturamos el inicio de session   
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    lastEm     = CambioEmpres.objects.filter(Usuario_id=idUser).last()
    lastEm=lastEm.lastEm   
    despacho  = Operacion.objects.filter(empresa_id=lastEm,estatus='A').order_by('-id')
    serializer = DespachoSerializer(despacho, many=True)
     
    return Response(serializer.data)





class Despacho(TemplateView):
     template_name = "pages/despacho.html"
     success_url = '/'
     
     def get_context_data(self, **kwargs):
          s = SessionStore()
          s['last_login'] = self.request.user.pk
          s.create()
          REU             = RelacionEmpresa.objects.filter(Usuario_id=s['last_login'])       
          lastEm          = CambioEmpres.objects.filter(Usuario_id=s['last_login']).last()
          idlastEmpresa   = lastEm.lastEm
          RE              = Empresa.objects.filter(usuario=s['last_login'],id=int(idlastEmpresa))
         #totalOperacion  = Operacion.objects.filter(empresa_id=lastEm,estatus='A').order_by('-id')
          patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa)).values('integrante_id')
          allPatinador    = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa),id_integrante).values('nombres')
          #allPatinador    = Integrante
          
          print(allPatinador[0],3333333333333333333)
          context = super(Despacho, self).get_context_data(**kwargs)
          
          context['allPatinador']     = allPatinador      # todos los patinadores de la empresa
          context['nomEmpresa']       = REU  # nombre de todas las empresa
          context['nomEmpresaU']      = RE   # nombre de la empresa actual
          
          
          
          return context

class CreateDespacho(View):
    
    def  get(self, request):
        can_totalOP    = request.GET.get('can_totalOP', None)
        idReferenciaOP = request.GET.get('idReferenciaOP', None)
        idEmpresaOP    = int(request.GET.get('idEmpresaOP', None))
        idColorOP      = int(request.GET.get('idColorOP', None))
        idUserOP       = int(request.GET.get('idUserOP', None))
        nomOperacion   = request.GET.get('nomOperacion', None)
        estatus = 'A'
        obj = Operacion.objects.create(
            empresa_id     = idEmpresaOP,
            usuario_id     = idUserOP,
            nom_operacion  = "OP"+nomOperacion, 
            estatus        = estatus,
            color_id       = idColorOP,
            referencia_id  = idReferenciaOP,
            can_total      = can_totalOP
          
              
        )
    
        data = {
            'user': "user"
        } 
        return JsonResponse(data)
