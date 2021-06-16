from django.urls import path
from integrante.views import CreateIntegrante,DeleteIntegrante,UpdateIntegrante
from .views import integranteList

urlpatterns = [
    path('integrante-list/', integranteList, name="integrante-list"),
    path('integrante/crud/create/', CreateIntegrante.as_view(), name='Integrante_ajax_create'),
    path('integrante/crud/delete/', DeleteIntegrante.as_view(), name='Integrante_ajax_delete'),
    path('integrante/crud/Update/', UpdateIntegrante.as_view(), name='Integrante_ajax_update'),

]
