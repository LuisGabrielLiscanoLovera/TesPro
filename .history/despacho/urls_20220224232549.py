from django.urls import path
from .views import despachoList, CreateDespacho,Despachos

urlpatterns = [
    path('', Despachos.as_view(), name='despacho'),
    path('despacho-list/', despachoList, name="despacho-list"),
    path('despacho/crud/create/', CreateDespacho.as_view(), name='Despacho_ajax_create'),

]


