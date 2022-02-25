from django.urls import path
from .views import despachoList, CreateDespacho,Despacho

urlpatterns = [
    path('', Despacho.as_view(), name='despacho'),
    path('despacho-list/', despachoList, name="despacho-list"),
    path('des/create/', CreateDespacho, name='Despacho_ajax_create'),

]


