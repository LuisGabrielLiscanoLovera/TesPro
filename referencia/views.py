from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Referencia
from .forms import GeeksForm
# Create your views here.

#class GeeksFormView(LoginRequiredMixin,FormView):
    # specify the Form you want to use
  #  form_class = GeeksForm
      
    # sepcify name of template
  #  template_name = "home.html"
  
    # can specify success url
    # url to redirect after successfully
    # updating details
 #   success_url ="/thanks/"