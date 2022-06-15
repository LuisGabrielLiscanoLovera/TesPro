from django.urls import path
from rest_framework import routers
from acumulado.views import Acumulado, cerrarAcumulado, abrirAcumulado, AcumuladoHistorial, AcumuladoListHistorial, AcumuladoListValor, AcumuladoList, AcumuladoDataIntegranteValor, ValorAcumulado, deleteAllAcumulado, createAcumulado, createProAcumulado, AcumuladoDataIntegrante, AcumuladoListProc, deleteAcumulado

router = routers.DefaultRouter()
urlpatterns = [


    path('', Acumulado.as_view(), name='Acumulado'),
    path('valorAcumulado/', ValorAcumulado.as_view(), name='ValorAcumulado'),
    path('prodAcumulado-list/', AcumuladoList, name="prodAcumulado-list"),

    path('prodAcumulado-listValor/', AcumuladoListValor,
         name="prodAcumulado-listValor"),


    path('AcumuladoProc-list/', AcumuladoListProc, name="AcumuladoProc-list"),

    path('create/', createAcumulado, name="Acumulado_ajax_create"),
    path('cproAcumulado/', createProAcumulado, name="NewsproAcumulado"),
    path('dataAcumuladoInte-list/', AcumuladoDataIntegrante,
         name="dataAcumuladoInte-list"),
    path('dataAcumuladoInte-listValor/', AcumuladoDataIntegranteValor,
         name="dataAcumuladoInte-listValor"),
    path('eliminar_acumulado/<str:id>/',
         deleteAcumulado, name="delete-produccion"),
    path('cerrarAcumulado/', cerrarAcumulado, name='cerrarAcumulado'),
    #path('delete/all/', deleteAllAcumulado.as_view(), name='Acumulado_ajax_Alldelete'),
    path('deleteAllAcumuldo/', deleteAllAcumulado.as_view(),
         name='deleteAllAcumuldo'),
    #historial Acumulado-historial
    path('acumuladoHistorial', AcumuladoHistorial.as_view(),
         name='acumuladoHistorial'),
    path('prodAcumulado-listHistorial/', AcumuladoListHistorial,
         name="prodAcumulado-listHistorial"),
    path('abrirAcumulado/', abrirAcumulado, name='abrirAcumulado'),

]
