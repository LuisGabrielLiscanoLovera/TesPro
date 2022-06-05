from django.urls import path
from rest_framework import routers

from seguimientoOp.views import SeguimientoOp, operacionesListSeguimiento
router = routers.DefaultRouter()
urlpatterns = [

    path('', SeguimientoOp.as_view(), name='SeguimientoOp'),
    path('lista_operacionesSeguimiento/',
         operacionesListSeguimiento, name="operaciones-listSeguimiento"),
]
