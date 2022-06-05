# Create your views here
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from patinador.models import Patinador
from integrante.models import Integrante
from empresa.models import Empresa, RelacionEmpresa, CambioEmpres
from django.contrib.sessions.backends.db import SessionStore
from talla.models import Talla
from operacion.models import Operacion


class SeguimientoOp(LoginRequiredMixin,TemplateView):
    
    template_name = "pages/seguimientoOp.html"
    def get_context_data(self, **kwargs):        
        context = super(SeguimientoOp, self).get_context_data(**kwargs)
        s = SessionStore()
        s['last_login'] = self.request.user.pk
        s.create()
        AllEmpresa = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])
        lastEm = CambioEmpres.objects.filter(usuario_id=s['last_login']).last()
        Tallas = Talla.objects.filter(usuario=s['last_login'], empresa_id=int(lastEm.lastEm)).values('id', 'nom_talla', 'num_talla')
        EmpresaActual = Empresa.objects.filter(usuario=s['last_login'], id=int(lastEm.lastEm))
        Operaciones = Operacion.objects.filter(usuario=s['last_login'], empresa_id=int(lastEm.lastEm)).values('nom_operacion', 'id')
        context = super(SeguimientoOp, self).get_context_data(**kwargs)
        # aqui se obtiene el user id
        context['login_user_id'] = s['last_login']
        context['lastIdEmpresa'] = int(lastEm.lastEm)  # ids empresas
        context['allTalla'] = Tallas  # todaslas las tallas
        context['allOperaciones'] = Operaciones  # todaslas operaciones
        context['nomEmpresa'] = AllEmpresa  # nombre de todas las empresa
        # nombre de la empresa actual
        context['nomEmpresaU'] = EmpresaActual
        context['last_login'] = s['last_login']    # ultimo inicio de seccion
        try:
          patinadores = Patinador.objects.all().filter(usuario=s['last_login'], empresa_id=int(lastEm.lastEm)).values('integrante_id')
          allPatinadores = Integrante.objects.all().filter(usuario=s['last_login'], empresa_id=int(lastEm.lastEm), id=int(patinadores[0].get('integrante_id'))).values('nombres', 'apellidos', 'id')
            # todos los patinadores de la empresa
          context['allPatinador'] = allPatinadores
          return context
        finally:
          return context