# Create your views here
from django.views.generic.base import TemplateView
from django.views.generic.base import TemplateView as TVB
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
class Despacho(TemplateView):
     template_name = "pages/despacho.html"
     
     def get_context_data(self, **kwargs):
          REU             = RelacionEmpresa.objects.filter(Usuario_id=s['last_login'])       
          context = super(Despacho, self).get_context_data(**kwargs)
          context['nomEmpresa']       = REU