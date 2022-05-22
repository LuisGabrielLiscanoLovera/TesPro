import imp
from django.urls import path
from rest_framework import routers

from acumulado.views import Acumulado,ProdAcomuladoList,createAcumulado

router = routers.DefaultRouter()
urlpatterns = [
 
   path('', Acumulado.as_view(), name='Acumulado'),
   path('prodAcomulado-list/', ProdAcomuladoList, name="prodAcomulado-list"),
   path('create/', createAcumulado, name="Acumulado_ajax_create"),
  
]


