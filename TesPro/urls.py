from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from segimientoOp.views import SegimientoOp
from destajo.views import Destajo
from casino.views import Casino
from acumulado.views import Acumulado
from despacho.views import Despacho
from xtarea.views import Xtarea
from home.views import Home

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),    
    path('auth/', include('authapp.urls')),   
    path('SegimientoOp/', SegimientoOp.as_view(), name='SegimientoOp'),
    path('Destajo/', Destajo.as_view(), name='Destajo'),
    path('Casino/', Casino.as_view(), name='Casino'),
    path('Acumulado/', Acumulado.as_view(), name='Acumulado'),
    path('Despacho/', Despacho.as_view(), name='Despacho'),
    path('Xtarea/', Xtarea.as_view(), name='Xtarea'),
    #apis rest-framework urls
    path('rf', include(router.urls)),#eliminar
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('api.urls')),
    path('referencia/', include('referencia.urls')),
    path('color/', include('color.urls')),
    path('tarea/', include('tarea.urls')),
    path('integrante/', include('integrante.urls')),
    
    
    
 ]



