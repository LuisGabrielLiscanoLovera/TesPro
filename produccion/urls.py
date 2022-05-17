import imp
from django.urls import path
from rest_framework import routers

from produccion.views import Produccion,ProduccionOPList,createProduccion,deleteProduccion
router = routers.DefaultRouter()
urlpatterns = [
 
   path('', Produccion.as_view(), name='produccion'),
   path('produccionOP-list/', ProduccionOPList, name="produccionOP-list"),
   path('create/', createProduccion, name="newProduccion"),
   path('eliminar_produccion/<str:id>/', deleteProduccion, name="delete-produccion")

]


