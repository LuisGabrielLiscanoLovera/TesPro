from django.urls import path
from despacho.views import despachoList
from .views import CreateDespacho,Despacho


urlpatterns = [
    path('despachos/', Despacho.as_view(), name='despacho'),
    
    path('despacho-list/', despachoList, name="despacho-list"),
    
    path('despachocreate/',CreateDespacho,name="despacho-list")
    
    #path('operacion/crud/delete/', DeleteOperacion.as_view(), name='Operacion_ajax_delete'),
    #path('operacion/crud/Update/', UpdateOperacion.as_view(), name='Operacion_ajax_update'),



]
