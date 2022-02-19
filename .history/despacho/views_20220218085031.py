# Create your views here
from django.views.generic.base import TemplateView

class Despacho(TemplateView):
     template_name = "pages/despacho.html"
     