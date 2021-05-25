from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.base import TemplateView as TVB
from django.views.generic import TemplateView, View, DeleteView
from empresa.models import Empresa,RelacionEmpresa
from django.contrib.auth.decorators import login_required

class Home(LoginRequiredMixin,TVB):
    template_name = "home.html"
    login_url = 'auth/signin/'
    success_url = '/' 
    def get_context_data(self, **kwargs):
        REU=RelacionEmpresa.objects.filter(Usuario_id=self.request.user.pk)
        RE=RelacionEmpresa.objects.filter(Usuario_id=self.request.user.pk)[:1]

        context = super(Home, self).get_context_data(**kwargs)        
        context['id'] = self.kwargs.get('id')
        context['login_user_id'] = self.request.user.pk #--aqui se obtiene el user id
        context['msg'] = u'Hello blog!'
        #context['empresa']  = RelacionEmpresa.objects.filter(Usuario_id=self.request.user.pk)
        context['nomEmpresa']=REU
        context['nomEmpresaU']=RE
        
        print (context)
        return context 


