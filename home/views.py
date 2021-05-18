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



from django.urls import reverse_lazy
from .models import CrudUser

from django.core import serializers
from django.http import JsonResponse


class CrudView(TemplateView):
    template_name = 'pages/despacho.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CrudUser.objects.all()
        return context


class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)