from django.urls import path
from despacho.views import despachoList, CreateDespacho

urlpatterns = [

    path('despacho-list/', despachoList, name="despacho-list"),
    path('despacho/crud/create/', CreateDespacho.as_view(), name='Despacho_ajax_create'),

]





