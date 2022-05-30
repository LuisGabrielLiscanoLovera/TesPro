from django.urls import path
from blackbox.views import DespachoPatinador,AcumuladoListProcPatinador,AcumuladoDataIntegrantePatinador,TallaEmpresaListPatinador,createProduccionPatinador,patinadoresActProdPatinador,integranteListPatinador,TareaListPatinador,ProduccionOPListPatinador,ItemListViewPatinador,ProduccionDataIntegrantePatinador,createDespachoPatinador,TallaOpCanIncosistentePatinadores,TallaOPListPatinador,casinoListPatinador,CasinoHomePatinador,AcumuladoPatinador,AcumuladoListPatinadores,operacionesListPatinadores,ProduccionPatinador,produccionesListPatinadores
urlpatterns = [
   path('despachoPatinador/', DespachoPatinador.as_view(), name='despachoPatinador'),
   path('lista_operacionesPatinador/', operacionesListPatinadores, name="operacionesListPatinadores"),
   path('tallaOP-list-patinador/', TallaOPListPatinador, name="tallaOP-list-patinador"),
   path('tallaOP-IncosistentePatinadores/', TallaOpCanIncosistentePatinadores, name="tallaOP-IncosistentePatinadores"),
   path('createPatinador/', createDespachoPatinador, name="newDespachoPatinador"),
   path('dataPatinador/', ItemListViewPatinador.as_view()),  
   
   path('produccionPatinador/', ProduccionPatinador.as_view(), name='produccionPatinador'),
   path('lista_produccionesPatinador/', produccionesListPatinadores, name="produccionListPatinadores"),
   path('dataProduccionInte-listPatinador/', ProduccionDataIntegrantePatinador, name="dataProduccionInte-listPatinador"),
   path('produccionOP-listPatinador/', ProduccionOPListPatinador, name="produccionOP-listPatinador"),
   path('tarea-listPatinador/', TareaListPatinador, name="tarea-listPatinador"),
   path('integrante-listPatinador/', integranteListPatinador, name="integrante-listPatinador"),
   path('lista_patinadoresAct-prodPatinador/', patinadoresActProdPatinador, name="patinadoresAct-list-prodPatinador"),
   path('createPatinadorProduccion/', createProduccionPatinador, name="newProduccionPatinador"),
   
   path('acumuladoPatinador/', AcumuladoPatinador.as_view(), name='acumuladoPatinador'),
   path('prodAcumulado-list-patinadores/', AcumuladoListPatinadores, name="prodAcumulado-list-patinadores"),
   path('tallaEmpresa-listPatinador/', TallaEmpresaListPatinador, name="tallaEmpresa-listPatinador"),
   path('dataAcumuladoInte-listPatinador/', AcumuladoDataIntegrantePatinador, name="dataAcumuladoInte-listPatinador"),
   path('AcumuladoProc-listPatinador/', AcumuladoListProcPatinador, name="AcumuladoProc-listPatinador"),
   
  
   
   path('casinoPatinador/', CasinoHomePatinador.as_view(), name='casinoPatinador'),
   path('casinoListPatinador/', casinoListPatinador, name="casinoListPatinador"),

] 