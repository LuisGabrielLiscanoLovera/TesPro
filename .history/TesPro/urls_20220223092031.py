from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from segimientoOp.views import SegimientoOp
from destajo.views import Destajo
from casino.views import CasinoTemplate
from acumulado.views import Acumulado
from despacho.views import Despacho
from xtarea.views import Xtarea
from home.views import Home,cambioEmpresa,SinEmpresa
from . import views


urlpatterns = [
    
    
    path('admin', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('sinEmpresa', SinEmpresa.as_view(), name='sinEmpresa'),

    path('auth/', include('authapp.urls')),   
    path('SegimientoOp/', SegimientoOp.as_view(), name='SegimientoOp'),
    path('Destajo/', Destajo.as_view(), name='Destajo'),
    path('Acumulado/', Acumulado.as_view(), name='Acumulado'),
    path('Despacho/', Despacho.as_view(), name='Despacho'),
    path('Xtarea/', Xtarea.as_view(), name='Xtarea'),
    

   
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), #apis rest-framework urls
    
    path('tarea/', include('tarea.urls')),    
    #path('prenda/', include('prenda.urls')),
    path('operacion/', include('operacion.urls')),
    path('talla/', include('talla.urls')),                      #listo.    
    path('casino/', include('casino.urls')),#casi listo 85%
    path('patinador/', include('patinador.urls')),              #listo
    path('integrante/', include('integrante.urls')),            #listo
    path('referencia/', include('referencia.urls')),            #listo
    path('color/', include('color.urls')),                      #listo.    
    path('cambioEmpresa/',cambioEmpresa, name='cambioEmpresa'), #listo 
    path('cambioE/',cambioEmpresa, name='cambioEmpresa'), #listo 
    
     ]