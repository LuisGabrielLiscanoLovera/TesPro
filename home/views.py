from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.base import TemplateView
from empresa.models import Empresa
from django.contrib.auth.decorators import login_required

class Home(LoginRequiredMixin,TemplateView):
    template_name = "home.html"
    login_url = 'auth/signin/'
    success_url = '/' 
    def get_context_data(self, **kwargs):
        
        context = super(Home, self).get_context_data(**kwargs)        
        context['id'] = self.kwargs.get('id')
        context['login_user_id'] = self.request.user.pk #--aqui se obtiene el user id
        context['msg'] = u'Hello blog!'
        context['empresa']  = Empresa.objects.filter(user_id=self.request.user.pk)
    
        return context 
