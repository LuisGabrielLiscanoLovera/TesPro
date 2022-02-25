from django.urls import path
from despacho.views import despachoList
from .views import CreateDespacho

urlpatterns = [
    path('despacho-list/', despachoList, name="despacho-list"),
    path('create/', CreateDespacho.as_view(), name='despacho_create'),
    #path('operacion/crud/delete/', DeleteOperacion.as_view(), name='Operacion_ajax_delete'),
    #path('operacion/crud/Update/', UpdateOperacion.as_view(), name='Operacion_ajax_update'),


]
