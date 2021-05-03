from django.contrib import admin
from django.urls import path,include

from segimientoOp.views import SegimientoOp
from destajo.views import Destajo
from casino.views import Casino
from acumulado.views import Acumulado
from despacho.views import Despacho
from xtarea.views import Xtarea
from home.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    
    path('auth/', include('authapp.urls')),   
    path('SegimientoOp/', SegimientoOp.as_view(), name='SegimientoOp'),
    path('Destajo/', Destajo.as_view(), name='Destajo'),
    path('Casino/', Casino.as_view(), name='Casino'),
    path('Acumulado/', Acumulado.as_view(), name='Acumulado'),
    path('Despacho/', Despacho.as_view(), name='Despacho'),
    path('Xtarea/', Xtarea.as_view(), name='Xtarea')
    
    
    
    
 ]


