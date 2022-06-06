# Create your views here
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from yaml import serialize
from patinador.models import Patinador
from integrante.models import Integrante
from empresa.models import Empresa, RelacionEmpresa, CambioEmpres
from django.contrib.sessions.backends.db import SessionStore
from talla.models import Talla, CanTalla
from operacion.models import Operacion
from authapp.models import MyUser
from operacion.serializers import OperacionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from produccion.models import Produccion
from talla.serializers import  CanTallaSerializer
from .serializers import ProdIntegranSeguimiento, PatinadorSerializer

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
          
          
@api_view(['GET'])
def operacionesListSeguimiento(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = CambioEmpres.objects.filter(usuario_id=idUser).last()
    despacho = Operacion.objects.filter(
        empresa_id=lastEm.lastEm, usuario_id=idUser).order_by('-id')
    serializer = OperacionSerializer(despacho, many=True)

    return Response(serializer.data)



@api_view(['GET'])  
def TallaOPListSeguimiento(request):
    if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)             
    lastEm   = CambioEmpres.objects.filter(usuario_id=idUser.id).last() 
    ptalla   = CanTalla.objects.filter(empresa_id=lastEm.lastEm,operacion_id=int(request.GET.get('idOp', None))).order_by('-id')
    serializer = CanTallaSerializer(ptalla, many=True)
    return Response(serializer.data)
 


@api_view(['GET'])
def IntegranteOPListSeguimiento(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)
    lastEm = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
    
    idOperacionSeguimiento = request.GET.get('idOperacionSeguimiento', None)
    #objects.distinct()
    pIntegrante = Produccion.objects.filter(empresa_id=lastEm.lastEm,
    operacion_id=idOperacionSeguimiento,usuario_id=idUser.id).distinct('integrante_id')
    serializer = ProdIntegranSeguimiento(pIntegrante, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def PatinadoresOPListSeguimiento(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)
    lastEm = CambioEmpres.objects.filter(usuario_id=idUser.id).last()

    idOperacionSeguimiento = request.GET.get('idOperacionSeguimientoP', None)
    #objects.distinct()
    
    pPatinador = Produccion.objects.filter(empresa_id=lastEm.lastEm,
                                            operacion_id=idOperacionSeguimiento, usuario_id=idUser.id).distinct('patinador_id')
    serializer = PatinadorSerializer(pPatinador, many=True)
    return Response(serializer.data)
