# Create your views here
from django.contrib.sessions.backends.db import SessionStore
from django.views.generic.base import TemplateView
from django.views.generic.base import TemplateView as TVB
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from integrante.models import Integrante
from patinador.models import Patinador
from talla.models import Talla
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
          AllEmpresa      = RelacionEmpresa.objects.filter(Usuario_id=s['last_login'])       
          lastEm          = CambioEmpres.objects.filter(Usuario_id=s['last_login']).last()
          
          Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('id','nom_talla','num_talla')
          EmpresaActual   = Empresa.objects.filter(usuario=s['last_login'],id=int(lastEm.lastEm))
          Operaciones     = Operacion.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),estatus='A').values('nom_operacion','id')
          patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('integrante_id')
          allPatinadores  = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),id=int(patinadores[0].get('integrante_id'))).values('nombres','apellidos','id')
          
          
          context = super(Despacho, self).get_context_data(**kwargs)          
          context['allTalla']        = Tallas     #todaslas las tallas
          context['allOperaciones']   = Operaciones     #todaslas operaciones 
          context['allPatinador']     = allPatinadores  #todos los patinadores de la empresa
          context['nomEmpresa']       = AllEmpresa      #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual   # nombre de la empresa actual
          
          
          
          
          return context

class CreateDespacho(View):
    
    def  get(self, request):
        idPatinador      = int(request.GET.get('idPatinador', None))
        idOperacion      = int(request.GET.get('idOperacion', None))
        idTalla          = int(request.GET.get('idTalla', None))
        idEmpresaOP      = int(request.GET.get('idEmpresaOP', None))
        idUserOP         = int(request.GET.get('idUserOP', None))
        cantidadRegistar = int(request.GET.get('cantidadRegistar', None))   
        
        estatus = 'A'
        obj = Despacho.objects.create(
            empresa_id     = idEmpresaOP,
            usuario_id     = idUserOP,
            peracion_id    = idOperacion, 
            idTalla        = idTalla,
            idPatinador    = idPatinador,
            
            can_total      = cantidadRegistar
          
              
        )
    
        data = {
            'user': "user"
        } 
        return JsonResponse(data)


