import imp
from django.urls import path
from rest_framework import routers

from acumulado.views import Acumulado,AcumuladoList,createAcumulado,createProAcumulado,AcumuladoDataIntegrante,AcumuladoListProc,deleteAcumulado

router = routers.DefaultRouter()
urlpatterns = [
 
   path('', Acumulado.as_view(), name='Acumulado'),
   path('prodAcumulado-list/', AcumuladoList, name="prodAcumulado-list"),
   path('AcumuladoProc-list/', AcumuladoListProc, name="AcumuladoProc-list"),

   path('create/', createAcumulado, name="Acumulado_ajax_create"),
   path('cproAcumulado/', createProAcumulado, name="NewsproAcumulado"),
   path('dataAcumuladoInte-list/', AcumuladoDataIntegrante, name="dataAcumuladoInte-list"),
   path('eliminar_acumulado/<str:id>/', deleteAcumulado, name="delete-produccion")


]