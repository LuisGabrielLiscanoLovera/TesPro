from django.urls import path
from casino.views import casinoList,createCasino 
urlpatterns = [
   
   path('casino-list/', casinoList, name="casino-list"),
   path('create/', createCasino, name="Casino_ajax_create"),

]