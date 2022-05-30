from django.urls import path
from blackbox.views import DespachoPatinador,createDespachoPatinador,TallaOpCanIncosistentePatinadores,TallaOPListPatinador,casinoListPatinador,CasinoHomePatinador,AcumuladoPatinador,AcumuladoListPatinadores,operacionesListPatinadores,ProduccionPatinador,produccionesListPatinadores
urlpatterns = [
   path('despachoPatinador/', DespachoPatinador.as_view(), name='despachoPatinador'),
   path('lista_operacionesPatinador/', operacionesListPatinadores, name="operacionesListPatinadores"),
   path('tallaOP-list-patinador/', TallaOPListPatinador, name="tallaOP-list-patinador"),
   path('tallaOP-IncosistentePatinadores/', TallaOpCanIncosistentePatinadores, name="tallaOP-IncosistentePatinadores"),
   path('createPatinador/', createDespachoPatinador, name="newDespachoPatinador"),

   
   
   
   path('acumuladoPatinador/', AcumuladoPatinador.as_view(), name='acumuladoPatinador'),
   path('prodAcumulado-list-patinadores/', AcumuladoListPatinadores, name="prodAcumulado-list-patinadores"),

   
   path('produccionPatinador/', ProduccionPatinador.as_view(), name='produccionPatinador'),
   path('lista_produccionesPatinador/', produccionesListPatinadores, name="produccionListPatinadores"),
   
   
   path('casinoPatinador/', CasinoHomePatinador.as_view(), name='casinoPatinador'),
   path('casinoListPatinador/', casinoListPatinador, name="casinoListPatinador"),

] 