# Create your views here
from django.views.generic.base import TemplateView
from django.views.generic.base import TemplateView as TVB

class Despacho(TemplateView):
     template_name = "pages/despacho.html"
     