from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django import views
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect, render
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from despacho.models import Despacho
from integrante.models import Integrante
from patinador.models import Patinador
from talla.models import Talla,CanTalla
from django.db.models import Sum, F 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authapp.models import MyUser
from despacho.serializers import DespachoSerializer,OperacionSerializer
from patinador.serializers import PatinadorSerializer
from operacion.models import Operacion
from django.views.generic import View
from django.http import JsonResponse, Http404, HttpResponse
from django.db.models import F
from django_serverside_datatable.views import ServerSideDatatableView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.



class DespachoPatinador(LoginRequiredMixin,TemplateView):
     
     template_name = "pages/despachoPerfilPatinador.html"
     success_url = '/'     
     def get_context_data(self, **kwargs):
          context = super(DespachoPatinador, self).get_context_data(**kwargs)
          s = SessionStore()
          s['last_login'] = self.request.user.pk
          s.create()
          lastEm=Integrante.objects.filter(id=s['last_login']).values('empresa_id')
          lastEm=int(lastEm[0]['empresa_id'])
          
          AllEmpresa      = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])          
          Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=lastEm).values('id','nom_talla','num_talla')
          EmpresaActual   = Empresa.objects.filter(usuario=s['last_login'],id=int(lastEm))
          Operaciones     = Operacion.objects.filter(usuario=s['last_login'],empresa_id=lastEm,estatus='A').values('nom_operacion','id')
          context = super(DespachoPatinador, self).get_context_data(**kwargs)
          context['login_user_id']    = s['last_login']   # aqui se obtiene el user id
          context['lastIdEmpresa']    = int(lastEm) # ids empresas
          context['allTalla']         = Tallas             #todaslas las tallas
          context['allOperaciones']   = Operaciones        #todaslas operaciones 
          context['nomEmpresa']       = AllEmpresa         #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual      # nombre de la empresa actual
          context['last_login']       = s['last_login']    # ultimo inicio de seccion
          try:
              patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=lastEm).values('integrante_id')
              allPatinadores  = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=lastEm,id=int(patinadores[0].get('integrante_id'))).values('nombres','apellidos','id')
              context['allPatinador']     = allPatinadores     #todos los patinadores de la empresa
              return context
          finally:
            return context
    
    
    
    
@api_view(['GET'])  
def operacionesListPatinadores(request):     
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
    
    lastEm=Integrante.objects.filter(id=idUser.id).values('empresa_id')
    lastEm=int(lastEm[0]['empresa_id'])
    #vamos bien
    despacho   = Operacion.objects.filter(empresa_id=lastEm,estatus='A').order_by('-id')
    serializer = OperacionSerializer(despacho, many=True)
    print(despacho)
    return Response(serializer.data)

