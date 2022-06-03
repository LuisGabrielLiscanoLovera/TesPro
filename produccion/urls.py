from django.urls import path
from rest_framework import routers

from produccion.views import Produccion, operacionesListValor, ProduccionHistorial, deleteAllProduccion, ProduccionDataIntegranteValor, ProduccionOPList, ValorProduccion, createProduccion, deleteProduccion, ProduccionDataIntegrante, patinadoresActProd
router = routers.DefaultRouter()
urlpatterns = [
 
   path('', Produccion.as_view(), name='produccion'),
   path('ValorProduccion', ValorProduccion.as_view(), name='ValorProduccion'),
   path('lista_operacionesValor/', operacionesListValor, name="operaciones-listValor"),
   
   path('produccionOP-list/', ProduccionOPList, name="produccionOP-list"),
   path('dataProduccionInte-list/', ProduccionDataIntegrante, name="dataProduccionInte-list"),
   path('dataProduccionInte-listValor/', ProduccionDataIntegranteValor, name="dataProduccionInte-listValor"),

   path('lista_patinadoresAct-prod/', patinadoresActProd, name="patinadoresAct-list-prod"),
   path('create/', createProduccion, name="newProduccion"),
   path('eliminar_produccion/<str:id>/', deleteProduccion, name="delete-produccion"),

#historial
   path('produccionHistorial', ProduccionHistorial.as_view(), name='produccionHistorial'),
   path('deleteAllProduccion/', deleteAllProduccion.as_view(), name='deleteAllProduccion'),
]


