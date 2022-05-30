from django.contrib import admin
from django.urls import path,include
from segimientoOp.views import SegimientoOp
from destajo.views import Destajo
from xtarea.views import Xtarea
from home.views import Home,cambioEmpresa,SinEmpresa
from . import views


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),#borarrrar menu debuguer
    
    path('admin', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('sinEmpresa', SinEmpresa.as_view(), name='sinEmpresa'),
    path('auth/', include('authapp.urls')),   
    path('SegimientoOp/', SegimientoOp.as_view(), name='SegimientoOp'),
    path('Destajo/', Destajo.as_view(), name='Destajo'),
    path('Xtarea/', Xtarea.as_view(), name='Xtarea'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), #apis rest-framework urls
    path('tarea/', include('tarea.urls')),                      #listo
    path('operacion/', include('operacion.urls')),              #listo
    path('talla/', include('talla.urls')),                      #listo   
    path('casino/', include('casino.urls')),                    #listo
    path('patinador/', include('patinador.urls')),              #listo
    path('integrante/', include('integrante.urls')),            #listo
    path('referencia/', include('referencia.urls')),            #listo
    path('color/', include('color.urls')),                      #listo
    path('cambioEmpresa/',cambioEmpresa, name='cambioEmpresa'), #listo 
    path('despacho/',  include('despacho.urls')),               #listo 
    path('produccion/',  include('produccion.urls')),           #listo 
    path('acumulado/',  include('acumulado.urls')),             #lusto
    path('blackbox/',  include('blackbox.urls')), 
    
     ]