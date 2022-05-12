# Create your views here
from django.views.generic.base import TemplateView

class Produccion(TemplateView):
     template_name = "pages/produccion.html"