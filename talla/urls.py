from django.urls import path
from talla.views import CreateTalla,DeleteTalla,UpdateTalla,TallaList

urlpatterns = [
    path('talla-list/', TallaList, name="talla-list"),
    path('talla/crud/create/', CreateTalla.as_view(), name='Talla_ajax_create'),
    path('talla/crud/delete/', DeleteTalla.as_view(), name='Talla_ajax_delete'),


]
