from django.urls import path
#from casino.views import CreateCasino,DeleteCasino,UpdateCasino
from .views import casinoList,CreateCasino  

urlpatterns = [
    path('casino-list/', casinoList, name="casino-list"),
    path('casino/crud/create/', CreateCasino.as_view(), name='Casino_ajax_create'),
    #path('Casino/crud/delete/', DeleteCasino.as_view(), name='Casino_ajax_delete'),
   # path('casino/crud/Update/', UpdateCasino.as_view(), name='Casino_ajax_update'),

]