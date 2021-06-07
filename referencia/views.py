from django.shortcuts import render
from django.urls import reverse_lazy
from referencia.models import Referencia,SimpleTable
from django.views.generic import TemplateView, View, DeleteView
from django.core import serializers
from django.http import JsonResponse
import django_tables2 as tables
from .models import CrudUser
from django.utils import (dateformat, formats)


class ReferenciaView(tables.SingleTableView):
    table_class = SimpleTable
    queryset = Referencia.objects.all()
    template_name = 'pages/referencia.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['referencias'] = Referencia.objects.all()
       
        return context


class CreateReferenciaUser(View):
    def  get(self, request):
        
        nom_referencia1 = request.GET.get('nom_referencia', None)
        descripcion1 = request.GET.get('descripcion', None)
       # print (nom_referencia1,descripcion1)
        obj = Referencia.objects.create(
            
            nom_referencia = nom_referencia1,
            descripcion = descripcion1
        )
        obj = Referencia.objects.latest('id')

        


        user = {'id':obj.id,'nom_referencia':obj.nom_referencia,'descripcion':obj.descripcion,'created_at':obj.created_at.strftime("%Y-%m-%d %H:%M:%S")}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteReferenciaUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Referencia.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateReferenciaUser(tables.SingleTableView):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        nom_referencia1 = request.GET.get('nom_referencia', None)
        descripcion1 = request.GET.get('descripcion', None)

        obj = Referencia.objects.get(id=id1)
        obj.name = name1
        obj.nom_referencia = nom_referencia1
        obj.descripcion = descripcion1
        obj.save()
        obj = Referencia.objects.latest('id')
        user = {'id':obj.id,'nom_referencia':obj.nom_referencia,'descripcion':obj.descripcion,'created_at':obj.created_at.strftime("%Y-%m-%d %H:%M:%S")}

        data = {
            'user': user
        }
        return JsonResponse(data)







class CrudView(TemplateView):
    template_name = 'pages/referencia.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CrudUser.objects.all()

        return context


class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)
        print("ddddddddddddddddddddddddddddddddddddddddddds")
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
        print('uuuuuuuuuuuuuuuuuppppppppppppppppdddddddddddddtttttttttttt')

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



# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import ReferenciaSerializer
# from django.contrib.auth.decorators import login_required
# from .models import Referencia
# # Create your views here.


# class Referencia(TemplateView):
#      template_name = "pdescripcions/referencia.html"



# class CrudView(TemplateView):
#     template_name = 'crud_ajax/crud.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['users'] = Referencia.objects.all()
#         return context



# @api_view(['GET'])
# def apiOverview(request):
# 	api_urls = {
# 		'List':'/Referencia-list/',
# 		'Detail View':'/Referencia-detail/<str:pk>/',
# 		'Create':'/Referencia-create/',
# 		'Update':'/Referencia-update/<str:pk>/',
# 		'Delete':'/Referencia-delete/<str:pk>/',
# 		}
# 	return Response(api_urls)
# #@login_required(login_url='signin')
# @api_view(['GET'])
# def referenciaList(request):
# 	referencias = Referencia.objects.all().order_by('-id')
# 	serializer = ReferenciaSerializer(referencias, many=True)
# 	return Response(serializer.data)





# #@login_required(login_url='signin')
# @api_view(['GET'])
# def referenciaDetail(request, pk):
# 	referencias = Referencia.objects.get(id=pk)
# 	serializer = ReferenciaSerializer(referencias, many=False)
# 	return Response(serializer.data)

# #@login_required(login_url='signin')
# @api_view(['POST'])
# def referenciaCreate(request):
# 	request.data._mutable = True
# 	request.data._mutable = False
# 	serializer = ReferenciaSerializer(data=request.data)
# 	print(type(request.data))
# 	print((request.data))
# 	if serializer.is_valid():
# 		print(type(request.data))
# 		print((request.data))
# 		serializer.save()
# 	return Response(serializer.data)




# #@login_required(login_url='signin')
# @api_view(['POST'])
# def referenciaUpdate(request, pk):
# 	referencia = Referencia.objects.get(id=pk)
# 	serializer = ReferenciaSerializer(instance=referencia, data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()
# 	return Response(serializer.data)

# #@login_required(login_url='signin')
# @api_view(['DELETE'])
# def referenciaDelete(request, pk):
# 	referencia = Referencia.objects.get(id=pk)
# 	referencia.delete()
# 	return Response('Item succsesfully delete!')
