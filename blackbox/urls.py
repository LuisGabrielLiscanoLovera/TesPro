from django.urls import path
from blackbox.views import DespachoPatinador
urlpatterns = [
   path('despachoPatinador', DespachoPatinador.as_view(), name='despachoPatinador'),
   
] 