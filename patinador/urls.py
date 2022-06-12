from django.urls import path
from patinador.views import CreatePatinador,DeletePatinador,UpdatePatinador
from .views import patinadorList

urlpatterns = [
    path('patinador-list/', patinadorList, name="patinador-list"),
    path('patinador/crud/create/', CreatePatinador.as_view(), name='Patinador_ajax_create'),
    path('patinador/crud/delete/', DeletePatinador.as_view(), name='Patinador_ajax_delete'),
    path('patinador/crud/Update/', UpdatePatinador.as_view(), name='Patinador_ajax_update'),


]

