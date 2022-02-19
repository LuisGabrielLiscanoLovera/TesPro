from pprint import pprint
from django.http import HttpResponseRedirect
from operacion.models import Operacion
from talla.models import Talla
from referencia.models import Referencia
from color.models import Color
from integrante.models import Integrante
from patinador.models import Patinador
from casino.models import Casino
from tarea.models import Tarea
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.base import TemplateView as TVB
from django.views.generic import TemplateView, View, DeleteView
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Sum
import re
from django.http import HttpResponse
from django.contrib.sessions.backends.db import SessionStore



class SinEmpresa(TVB):
    template_name = "pages/404.html"

class Home(LoginRequiredMixin,TVB):
    
    template_name = "home.html"
    login_url = 'auth/signin/'
    success_url = '/'
    
    
    def get_context_data(self, **kwargs):        
        s = SessionStore()
        s['last_login'] = self.request.user.pk
        s.create()
              
        REU             = RelacionEmpresa.objects.filter(Usuario_id=s['last_login'])       
        lastEm          = CambioEmpres.objects.filter(Usuario_id=s['last_login']).last()
        idlastEmpresa   = lastEm.lastEm
        RE=Empresa.objects.filter(usuario=s['last_login'],id=int(idlastEmpresa))
        print(RE)
        totalReferencia = Referencia.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa))
        totalColor      = Color.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa))
        totalIntegrante = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa))
        allTalla        = Talla.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa))
        allTarea        = Tarea.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa))
        totalPatinador  = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa)).count()
        totalOperacion  = Operacion.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa)).count()
        totalCasino     = Casino.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa))
        totalCasino     = totalCasino.aggregate(Sum('deuda'))
        totalCasino=re.sub("[^0-9]","",str(totalCasino))        
        context = super(Home, self).get_context_data(**kwargs)        
        context['id']               = self.kwargs.get('id')
        context['login_user_id']    = s['last_login']   # aqui se obtiene el user id
        context['nomEmpresa']       = REU                    # nombre de todas las empresa
        context['nomEmpresaU']      = RE                     # nombre de la empresa actual
        context['lastIdEmpresa']    = int(idlastEmpresa)     # ids empresas
        context['totalReferencia']  = totalReferencia.count()# total referencias
        context['totalColor']       = totalColor.count()     # total color
        context['totalIntegrante']  = totalIntegrante.count()# total integrante
        context['totalPatinadores'] = totalPatinador         # total patinador
        context['allIntegrante']    = totalIntegrante        # all integrante
        context['allTalla']         = allTalla               # all talla
        context['allReferencia']    = totalReferencia        # all referencia
        context['allColor']         = totalColor             # all color
        context['totalCasino']      = totalCasino            # total fondo casino
        context['totalOperacion']   = totalOperacion         # total operacion
        context['totalTallas']      = allTalla.count()       # total talla
        context['totalTarea']       = allTarea.count()       # total tarea

        return context
def cambioEmpresa(request):
    try:CambioEmpres.objects.order_by('-pk')[0].delete()
    except Exception as e:  print(str(e))
    idEmpresa = request.GET.get('idEmpresa', None)
    idUser    = request.GET.get('idUser', None)
    obj = CambioEmpres.objects.create(
            Usuario_id = idUser,
            lastEm = idEmpresa
            )
    return redirect('home')

    