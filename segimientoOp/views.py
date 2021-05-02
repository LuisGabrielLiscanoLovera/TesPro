from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
class SegimientoOp(ListView):
    template_name = "segimientoOp.html"
    
    