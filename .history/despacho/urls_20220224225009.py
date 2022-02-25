from django.urls import path
from .views import despachoList, CreateDespacho,Despacho

urlpatterns = [
    path('despachosssssss/', Despacho.as_view(), name='despacho'),
    path('despacho-list/', despachoList, name="despacho-list"),
    path('despacho/crud/create/', CreateDespacho, name='Despacho_ajax_create'),

]


