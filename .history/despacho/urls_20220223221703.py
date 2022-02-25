from django.urls import path
from despacho.views import despachoList
from .views import CreateDespacho,Despacho


urlpatterns = [
    path('despacho/', Despacho.as_view(), name='Despachos'),
    path('despacho-list/', despachoList, name="despacho-list"),
    path('despacho/crud/create/', CreateDespacho.as_view(), name='Despacho_ajax_create'),
    #path('operacion/crud/delete/', DeleteOperacion.as_view(), name='Operacion_ajax_delete'),
    #path('operacion/crud/Update/', UpdateOperacion.as_view(), name='Operacion_ajax_update'),


]
