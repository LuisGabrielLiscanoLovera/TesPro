from django.urls import path
from despacho.views import despachoList
from .views import CreateDespacho,Despacho


urlpatterns = [
    path('despachos/', Despacho.as_view(), name='despacho'),
    
    path('despacho-list/', despachoList, name="despacho-list"),
    path('/crud/create/', CreateDespacho.as_view(), name='Despacho_ajax_create'),
    #path('operacion/crud/delete/', DeleteOperacion.as_view(), name='Operacion_ajax_delete'),
    #path('operacion/crud/Update/', UpdateOperacion.as_view(), name='Operacion_ajax_update'),



]
