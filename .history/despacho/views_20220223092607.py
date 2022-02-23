# Create your views here
from django.contrib.sessions.backends.db import SessionStore
from django.views.generic.base import TemplateView
from django.views.generic.base import TemplateView as TVB
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authapp.models import MyUser
from .serializers import DespachoSerializer


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
    despacho  = despacho.objects.filter(empresa_id=lastEm).order_by('-id')
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
          RE=Empresa.objects.filter(usuario=s['last_login'],id=int(idlastEmpresa))
          context = super(Despacho, self).get_context_data(**kwargs)
                   
          context['nomEmpresa']       = REU  # nombre de todas las empresa
          context['nomEmpresaU']      = RE   # nombre de la empresa actual
          
          
          
          return context