from django.urls import path
from .views import casinoList,CreateCasino,UpdateCasino,casinoListImporte

urlpatterns = [
    path('casino-list/', casinoList, name="casino-list"),
    path('casinoImporte-list/', casinoListImporte, name="casinoImporte-list"),
    path('casino/crud/create/', CreateCasino.as_view(), name='Casino_ajax_create'),
    #path('Casino/crud/delete/', DeleteCasino.as_view(), name='Casino_ajax_delete'),
    path('casino/crud/Update/', UpdateCasino.as_view(), name='Casino_ajax_update'),

]