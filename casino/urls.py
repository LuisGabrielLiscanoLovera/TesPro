from django.urls import path
from casino.views import casinoList,createCasino,deleteImporteUnico,CasinoDataIntegranteImporte,CasinoDataImporte,patinadoresActCasino,createProCasino,TotalImporteInte
urlpatterns = [
   
   path('casino-list/', casinoList, name="casino-list"),
   path('create/', createCasino, name="Casino_ajax_create"),
   path('dataCasinoInte-list/', CasinoDataIntegranteImporte, name="dataCasinoInte-list"),
   path('dataCasino-list/', CasinoDataImporte, name="dataCasino-list"),

   path('lista_patinadoresAct-casino/', patinadoresActCasino, name="patinadoresAct-list-casino"),
   path('cproCasino/', createProCasino, name="NewsproCasino"),
   path('totalImporteInte/', TotalImporteInte, name="totalImporteInte"),
   path('deleteImporteUnico/<str:id>/', deleteImporteUnico, name="delete-produccion")

]