# Create your views here
from django.views.generic.base import TemplateView

class SegimientoOp(TemplateView):
     template_name = "pages/segimientoOp.html"
     
     #crear un contador de tareas d toda la operacion