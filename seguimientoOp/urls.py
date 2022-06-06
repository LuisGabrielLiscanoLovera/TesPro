from django.urls import path
from rest_framework import routers

from seguimientoOp.views import SeguimientoOp, operacionesListSeguimiento, TallaOPListSeguimiento, IntegranteOPListSeguimiento
router = routers.DefaultRouter()
urlpatterns = [

    path('', SeguimientoOp.as_view(), name='SeguimientoOp'),
    path('lista_operacionesSeguimiento/',operacionesListSeguimiento, name="operaciones-listSeguimiento"),
    
    
    
    
    path('tallaOP-listSeguimiento/', TallaOPListSeguimiento, name="tallaOP-listSeguimiento"),
    #list of members who participated in the operation
    path('integranteOp-listSeguimiento/', IntegranteOPListSeguimiento,name="integranteOp-listSeguimiento"),
    
]
