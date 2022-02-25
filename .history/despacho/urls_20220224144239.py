from django.urls import path
from despacho.views import despachoList, CreateDespacho

urlpatterns = [
    path('integrante-list/', despachoList, name="integrante-list"),
    path('integrante/crud/create/', CreateDespacho.as_view(), name='Integrante_ajax_create'),
    #path('integrante/crud/delete/', DeleteIntegrante.as_view(), name='Integrante_ajax_delete'),
    #path('integrante/crud/Update/', UpdateIntegrante.as_view(), name='Integrante_ajax_update'),

]





#
#urlpatterns = [
 #   path('despacho/', Despacho.as_view(), name='despacho'),
    
  #  path('despacho-list/', despachoList, name="despacho-list"),
    
  #  path('despacho-create/',CreateDespacho.as_view(), name="crear_despacho")
    
    #path('operacion/crud/delete/', DeleteOperacion.as_view(), name='Operacion_ajax_delete'),
    #path('operacion/crud/Update/', UpdateOperacion.as_view(), name='Operacion_ajax_update'),



#]
