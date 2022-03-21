from django.urls import path
from talla.views import CreateTalla,DeleteTalla,TallaList
from talla.views import CreateTallaOP,DeleteTallaOP,TallaOPList

urlpatterns = [
    path('talla-list/', TallaList, name="talla-list"),
    path('talla/crud/create/', CreateTalla.as_view(), name='Talla_ajax_create'),
    path('talla/crud/delete/', DeleteTalla.as_view(), name='Talla_ajax_delete'),
    
    #para tallas de las op
    path('tallaOP-list/', TallaOPList, name="tallaOP-list"),
    path('tallaOP/crud/create/', CreateTallaOP.as_view(), name='TallaOP_ajax_create'),
    path('tallaOP/crud/delete/', DeleteTallaOP.as_view(), name='TallaOP_ajax_delete'),



]
