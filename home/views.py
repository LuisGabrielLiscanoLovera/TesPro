from referencia.models import Referencia
from color.models import Color
from integrante.models import Integrante
from patinador.models import Patinador

from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.base import TemplateView as TVB
from django.views.generic import TemplateView, View, DeleteView
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
class Home(LoginRequiredMixin,TVB):
    template_name = "home.html"
    login_url = 'auth/signin/'
    success_url = '/' 
        
    def get_context_data(self, **kwargs):
        REU      = RelacionEmpresa.objects.filter(Usuario_id=self.request.user.pk)
        print("llllllllllllll",REU)

        lastEm   = CambioEmpres.objects.values('lastEm').last()
        idlastEmpresa=lastEm.get("lastEm")
        #manejar el error  de last id
        RE=Empresa.objects.filter(id=int(idlastEmpresa))
        totalReferencia = Referencia.objects.all().filter(empresa_id=int(idlastEmpresa)).count()
        totalColor      = Color.objects.all().filter(empresa_id=int(idlastEmpresa)).count()
        totalIntegrante = Integrante.objects.all().filter(empresa_id=int(idlastEmpresa))
        totalPatinador  = Patinador.objects.all().filter(empresa_id=int(idlastEmpresa)).count()
       
        context = super(Home, self).get_context_data(**kwargs)        
        context['id']               = self.kwargs.get('id')
        context['login_user_id']    = self.request.user.pk  # aqui se obtiene el user id
        context['nomEmpresa']       = REU                   # nombre de todas las empresa
        context['nomEmpresaU']      = RE                    # nombre de la empresa actual
        context['lastIdEmpresa']    = int(idlastEmpresa)    # ids empresas
        context['totalReferencia']  = totalReferencia       # total referencias
        context['totalColor']       = totalColor            # total color
        context['totalIntegrante']  = totalIntegrante.count()# total integrante
        context['totalPatinadores'] = totalPatinador       # total patinador
        context['allIntegrante']    = totalIntegrante       # all integrante

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
    print(idUser,idEmpresa)
    return redirect('home')

    
