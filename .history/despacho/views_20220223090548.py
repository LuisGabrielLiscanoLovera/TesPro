# Create your views here
from django.contrib.sessions.backends.db import SessionStore
from django.views.generic.base import TemplateView
from django.views.generic.base import TemplateView as TVB
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres






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