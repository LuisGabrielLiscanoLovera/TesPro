from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from segimientoOp.views import SegimientoOp
from destajo.views import Destajo
from casino.views import CasinoTemplate
from acumulado.views import Acumulado
from despacho.views import Despacho
from xtarea.views import Xtarea
from home.views import Home,cambioEmpresa
from . import views

urlpatterns = [
    
    
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),    
    path('auth/', include('authapp.urls')),   
    path('SegimientoOp/', SegimientoOp.as_view(), name='SegimientoOp'),
    path('Destajo/', Destajo.as_view(), name='Destajo'),
    path('Casino/', CasinoTemplate.as_view(), name='Casino'),
    path('Acumulado/', Acumulado.as_view(), name='Acumulado'),
    path('Despacho/', Despacho.as_view(), name='Despacho'),
    path('Xtarea/', Xtarea.as_view(), name='Xtarea'),
    
   
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), #apis rest-framework urls
    
    path('tarea/', include('tarea.urls')),
    
    path('patinador/', include('patinador.urls')),
    path('prenda/', include('prenda.urls')),
    path('casino/', include('casino.urls')),
    
    path('integrante/', include('integrante.urls')),
    path('referencia/', include('referencia.urls')),            #crud creado
    path('color/', include('color.urls')),                      #crud creado.    
    path('cambioEmpresa/',cambioEmpresa, name='cambioEmpresa'), #listo    
     ]