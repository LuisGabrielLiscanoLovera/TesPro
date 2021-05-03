from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from empresa.models import Empresa
from django.contrib.auth.decorators import login_required

class Home(LoginRequiredMixin, TemplateView):
    template_name = "home.html"   
    
    def get_context_data(self, **kwargs):
        #empresa = Empresa.objects.filter(user=1)              
        context = super(Home, self).get_context_data(**kwargs)
        
        context['id'] = self.kwargs.get('id')
        context['login_user_id'] = self.request.user.pk #--aqui se obtiene el user id
           
       
        
        context['msg'] = u'Hello blog!'
        return context 
