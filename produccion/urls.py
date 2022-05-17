import imp
from django.urls import path
from rest_framework import routers

from produccion.views import Produccion,ProduccionOPList,createProduccion
router = routers.DefaultRouter()
urlpatterns = [
 
   path('', Produccion.as_view(), name='produccion'),
   path('produccionOP-list/', ProduccionOPList, name="produccionOP-list"),
   path('create/', createProduccion, name="newProduccion"),
]


