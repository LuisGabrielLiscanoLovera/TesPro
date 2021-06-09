from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.base import TemplateView as TVB
from django.views.generic import TemplateView, View, DeleteView
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
import json
from django.core.serializers.json import DjangoJSONEncoder
class Home(LoginRequiredMixin,TVB):
    template_name = "home.html"
    login_url = 'auth/signin/'
    success_url = '/' 
        
    def get_context_data(self, **kwargs):
        
        REU=RelacionEmpresa.objects.filter(Usuario_id=self.request.user.pk)
        #RE=RelacionEmpresa.objects.filter(Usuario_id=self.request.user.pk)[:1]
        #rree=RelacionEmpresa.objects.filter(Usuario_id=self.request.user.pk).all().values('Empresa_id')
        rree=RelacionEmpresa.objects.all().filter(Usuario_id=self.request.user.pk).values('Empresa_id')
    
        idUser=int(self.request.user.pk)        
        #rree = RelacionEmpresa.objects.all().values('Empresa').filter(Usuario_id=idUser)
        #lastEm=CambioEmpres.objects.values('lastEm').filter(Usuario_id=idUser).first()
       
        lastEm=CambioEmpres.objects.values('lastEm').last()
        
        RE=Empresa.objects.filter(id=lastEm.get("lastEm"))
       
        context = super(Home, self).get_context_data(**kwargs)        
        context['id'] = self.kwargs.get('id')
        context['login_user_id'] = self.request.user.pk #--aqui se obtiene el user id
        #context['empresa']  = RelacionEmpresa.objects.filter(Usuario_id=self.request.user.pk)
        context['nomEmpresa']=REU#nombre de todas las empresa
        context['nomEmpresaU']=RE#nombre de la empresa actual
        context['idEmpresa']=rree#ids empresas
        
        #context['idEmpresa'] = lastEm.get("lastEm")
        print ()
        return context

def cambioEmpresa(request):
    """ try:CambioEmpres.objects.order_by('-pk')[0].delete()
    except Exception as e:  print(str(e)) """
    print("ggggggggggggggggggg")
    idEmpresa = request.GET.get('idEmpresa', None)
    idUser    = request.GET.get('idUser', None)
    print("hhhhhhhhhhhhhhhh",idEmpresa,idUser)
    obj = CambioEmpres.objects.create(
            Usuario_id = idUser,
            lastEm = idEmpresa,
           
        )
    print(idUser,idEmpresa)
    return redirect('home')

    
