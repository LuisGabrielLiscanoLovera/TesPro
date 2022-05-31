import imp
from django.urls import path

from .views import despacho_list,Despachos,DespachosHistorial,operacionesListHistorial,deleteDespacho,operacionesList,patinadoresAct,createDespacho,ItemListView
from rest_framework import routers
router = routers.DefaultRouter()
urlpatterns = [

    path('lista_operaciones/', operacionesList, name="operaciones-list"),
    path('lista_patinadoresAct/', patinadoresAct, name="patinadoresAct-list"),

    path('', Despachos.as_view(), name='despacho'),
    path('list/', despacho_list, name="despachos"),
            
    path('data/', ItemListView.as_view()),  
    path('create/', createDespacho, name="newDespacho"),  
    path('eliminar_despachos/<str:id>/', deleteDespacho, name="delete-despacho"),
    
    
    
    #historial
    path('despachoHistorial', DespachosHistorial.as_view(), name='despachoHistorial'),
    path('lista_operacionesHistorial/', operacionesListHistorial, name="operaciones-listHistorial"),

]


