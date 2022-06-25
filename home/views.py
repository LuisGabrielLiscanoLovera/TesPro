
from operacion.models import Operacion
from talla.models import Talla
from referencia.models import Referencia
#from color.models import Color
from integrante.models import Integrante
from patinador.models import Patinador
from tarea.models import Tarea
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView as TVB
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from django.contrib.sessions.backends.db import SessionStore


class SinEmpresa(TVB):
    template_name = "pages/404.html"

class Home(LoginRequiredMixin,TVB):
    
    template_name = "home.html"
    login_url = 'auth/signin/'
    success_url = '/'  
    def get_context_data(self, **kwargs):
        s = SessionStore()
        s['last_login'] = self.request.user.id
        s.create()
        print(s['last_login'])
        lastEm          = CambioEmpres.objects.filter(usuario_id=s['last_login']).last()
       
      
        
        
        
       
        
        
        if lastEm==None:
            empresaId = Empresa.objects.filter(
                usuario_id=s['last_login']).values('id')
            physics = CambioEmpres(usuario_id=s['last_login'], lastEm=empresaId[0]['id'])
            physics.save()
            lastEm = CambioEmpres.objects.filter(
                usuario_id=s['last_login']).last()
        
        nomTodasEmpresa = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])   
        idlastEmpresa   = lastEm.lastEm
        
        
        #Carga de data por defecto Sin(Referenciam,color,talla)
        if Referencia.objects.filter(usuario_id=s['last_login'],empresa_id=idlastEmpresa,nom_referencia="SIN REFERENCIA"):pass
        else: Referencia.objects.create(nom_referencia = "SIN REFERENCIA",descripcion = "SIN REFERENCIA", empresa_id = lastEm.lastEm, usuario_id = s['last_login'])
        #if Color.objects.filter(usuario_id=s['last_login'],empresa_id=idlastEmpresa,nom_color="SIN COLOR"):pass
        #else: Color.objects.create(nom_color = "SIN COLOR",codigo_color = "0",empresa_id = lastEm.lastEm,usuario_id = s['last_login'])
        if Talla.objects.filter(usuario_id=s['last_login'],empresa_id=idlastEmpresa,nom_talla="SIN TALLA"):pass
        else:
            Talla.objects.create(empresa_id=lastEm.lastEm,usuario_id=s['last_login'],nom_talla="SIN TALLA",num_talla= 0,)
            obj = Talla.objects.latest('id')
            obj = Talla.objects.all().filter(id=obj.id).update(btnAddTalla="<input type='number' style='background-color : #f5f2f2;' class='form-control-sm input-group-number' name='inputTalla-{}'  id='inputTalla-{}'>".format(obj.id,obj.id))
        #-----------------------------------------------------
             
        nombreEpreAct   = Empresa.objects.filter(usuario=s['last_login'],id=int(idlastEmpresa))        
        totalReferencia = Referencia.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa))
       # totalColor      = Color.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa))
        totalIntegrante = Integrante.objects.all().filter(usuario=s['last_login'],estatus='A',empresa_id=int(idlastEmpresa))
        allTalla        = Talla.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa))
        allTarea        = Tarea.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa))
        totalPatinador  = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa)).count()
        totalOperacion  = Operacion.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa)).count()
        #totalCasino     = Casino.objects.all().filter(usuario=s['last_login'],empresa_id=int(idlastEmpresa))
        #totalCasino     = totalCasino.aggregate(Sum('deuda'))
        #totalCasino=re.sub("[^0-9]","",str(totalCasino))        
        
        context = super(Home, self).get_context_data(**kwargs)        
        context['id']               = self.kwargs.get('id')
        context['login_user_id']    = s['last_login']   # aqui se obtiene el user id
        context['nomEmpresa']       = nomTodasEmpresa               # nombre de todas las empresa
        context['nomEmpresaU']      = nombreEpreAct                 # nombre de la empresa actual
        context['lastIdEmpresa']    = int(idlastEmpresa)            # ids empresas
        context['totalReferencia']  = totalReferencia.count()-1     # total referencias (el -1 para no contar las sin referencia)
       # context['totalColor']       = totalColor.count()-1          # total color (el -1 para no contar las sin color)
        context['totalIntegrante']  = totalIntegrante.count()       # total integrante
        context['totalPatinadores'] = totalPatinador                # total patinador
        context['allIntegrante']    = totalIntegrante               # all integrante
        context['allTalla']         = allTalla                      # all talla
        context['allReferencia']    = totalReferencia               # all referencia
       # context['allColor']         = totalColor                    # all color
    #    context['totalCasino']      = totalCasino                   # total fondo casino
        context['totalOperacion']   = totalOperacion                # total operacion
        context['totalTallas']      = allTalla.count()-1            # total talla (el -1 para no contar las sin talla)
        context['totalTarea']       = allTarea.count()              # total tarea

        return context
def cambioEmpresa(request):
    try:CambioEmpres.objects.order_by('-pk')[0].delete()
    except Exception as e:  print(str(e))
    idEmpresa = request.GET.get('idEmpresa', None)
    idUser    = request.GET.get('idUser', None)
    obj = CambioEmpres.objects.create(
            usuario_id = idUser,
            lastEm = idEmpresa
            )
    return redirect('home')

