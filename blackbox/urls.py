from django.urls import path
from blackbox.views import DespachoPatinador,operacionesListPatinadores
urlpatterns = [
   path('despachoPatinador/', DespachoPatinador.as_view(), name='despachoPatinador'),
   path('lista_operacionesPatinador/', operacionesListPatinadores, name="operaciones-operacionesListPatinadores"),

] 