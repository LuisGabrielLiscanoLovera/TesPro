from django.urls import path
from despacho.views import despachoList
from .views import CreateDespacho

urlpatterns = [
    path('Despachos/', Despacho.as_view(), name='Despachos'),

    path('despacho-list/', despachoList, name="despacho-list"),
    path('despacho_create/', CreateDespacho.as_view(), name='despacho_create'),
    #path('operacion/crud/delete/', DeleteOperacion.as_view(), name='Operacion_ajax_delete'),
    #path('operacion/crud/Update/', UpdateOperacion.as_view(), name='Operacion_ajax_update'),


]
