from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.base import TemplateView as TVB
from django.views.generic import TemplateView, View, DeleteView
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from django.contrib.auth.decorators import login_required

class Home(LoginRequiredMixin,TVB):
    template_name = "home.html"
    login_url = 'auth/signin/'
    success_url = '/' 
        
    def get_context_data(self, **kwargs):
        
        REU=RelacionEmpresa.objects.filter(Usuario_id=self.request.user.pk)
        RE=RelacionEmpresa.objects.filter(Usuario_id=self.request.user.pk)[:1]
        # rree=RelacionEmpresa.objects.filter(Usuario_id=self.request.user.pk).all()
        idUser=int(self.request.user.pk)        
        #rree = RelacionEmpresa.objects.all().values('Empresa').filter(Usuario_id=idUser)
        
        context = super(Home, self).get_context_data(**kwargs)        
        context['id'] = self.kwargs.get('id')
        context['login_user_id'] = self.request.user.pk #--aqui se obtiene el user id
        context['msg'] = u'Hello blog!'
        #context['empresa']  = RelacionEmpresa.objects.filter(Usuario_id=self.request.user.pk)
        context['nomEmpresa']=REU#nombre de todas las empresa
        context['nomEmpresaU']=RE#la primera empresa
       # context['test']=rree#ids empresas
       
        print (context)
        return context 
    

def cambioEmpresa(request):
    idEmpresa = request.GET.get('idEmpresa', None)
    idUser    = request.GET.get('idUser', None)
    obj = CambioEmpres.objects.create(
            Usuario_id = idUser,
            lastEm = idEmpresa,
           
        )
    print(idUser,idEmpresa)
    return redirect('home')

    
