from django.urls import path
from despacho.views import despachoList, CreateDespacho,Despacho

urlpatterns = [
    path('despacho/', Despacho.as_view(), name='despacho'),
    path('despacho-list/', despachoList, name="despacho-list"),
    path('/despacho/crud/create/', CreateDespacho.as_view(), name='Despacho_ajax_create'),

]


