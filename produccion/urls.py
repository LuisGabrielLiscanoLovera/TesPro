import imp
from django.urls import path
from rest_framework import routers

from produccion.views import Produccion
router = routers.DefaultRouter()
urlpatterns = [
 
   path('', Produccion.as_view(), name='produccion'),
   
]


