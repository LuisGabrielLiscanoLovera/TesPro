from django.urls import path
from despacho.views import despachoList

urlpatterns = [
    path('operacion-list/', operacionList, name="operacion-list"),
  #  path('operacion/crud/create/', CreateOperacion.as_view(), name='Operacion_ajax_create'),
    path('operacion/crud/delete/', DeleteOperacion.as_view(), name='Operacion_ajax_delete'),
    path('operacion/crud/Update/', UpdateOperacion.as_view(), name='Operacion_ajax_update'),


]