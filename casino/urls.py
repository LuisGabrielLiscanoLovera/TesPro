from django.urls import path
from casino.views import casinoList,createCasino,CasinoDataIntegranteImporte
urlpatterns = [
   
   path('casino-list/', casinoList, name="casino-list"),
   path('create/', createCasino, name="Casino_ajax_create"),
   path('dataCasinoInte-list/', CasinoDataIntegranteImporte, name="dataCasinoInte-list"),

]