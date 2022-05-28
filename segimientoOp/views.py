# Create your views here
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
class SegimientoOp(LoginRequiredMixin,TemplateView):
     template_name = "pages/segimientoOp.html"
     
     #crear un contador de tareas d toda la operacion