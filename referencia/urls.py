from django.urls import path
from referencia.views import CreateReferencia,DeleteReferencia,UpdateReferencia
from .views import referenciaList

urlpatterns = [
    path('referencia-list/', referenciaList, name="referencia-list"),
    path('referencia/crud/create/', CreateReferencia.as_view(), name='Referencia_ajax_create'),
    path('referencia/crud/delete/', DeleteReferencia.as_view(), name='Referencia_ajax_delete'),
    path('crud/Update/', UpdateReferencia, name='Referencia_ajax_update'),

]
