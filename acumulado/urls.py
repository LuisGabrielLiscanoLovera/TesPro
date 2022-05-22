import imp
from django.urls import path
from rest_framework import routers

from acumulado.views import Acumulado,ProdAcomuladoList

router = routers.DefaultRouter()
urlpatterns = [
 
   path('', Acumulado.as_view(), name='Acumulado'),
   path('prodAcomulado-list/', ProdAcomuladoList, name="prodAcomulado-list"),
 
]


