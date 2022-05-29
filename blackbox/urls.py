from django.urls import path
from blackbox.views import DespachoPatinador,casinoListPatinador,CasinoHomePatinador,AcumuladoPatinador,AcumuladoListPatinadores,operacionesListPatinadores,ProduccionPatinador,produccionesListPatinadores
urlpatterns = [
   path('despachoPatinador/', DespachoPatinador.as_view(), name='despachoPatinador'),
   path('lista_operacionesPatinador/', operacionesListPatinadores, name="operacionesListPatinadores"),
   
   
   path('acumuladoPatinador/', AcumuladoPatinador.as_view(), name='acumuladoPatinador'),
   path('prodAcumulado-list-patinadores/', AcumuladoListPatinadores, name="prodAcumulado-list-patinadores"),

   
   path('produccionPatinador/', ProduccionPatinador.as_view(), name='produccionPatinador'),
   path('lista_produccionesPatinador/', produccionesListPatinadores, name="produccionListPatinadores"),
   
   
   path('casinoPatinador/', CasinoHomePatinador.as_view(), name='casinoPatinador'),
   path('casinoListPatinador/', casinoListPatinador, name="casinoListPatinador"),

] 