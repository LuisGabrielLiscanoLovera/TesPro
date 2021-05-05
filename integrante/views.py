# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import IntegranteSerializer
from django.contrib.auth.decorators import login_required
from .models import Integrante
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/Integrate-list/',
		'Detail View':'/Integrate-detail/<str:pk>/',
		'Create':'/Integrate-create/',
		'Update':'/Integrate-update/<str:pk>/',
		'Delete':'/Integrate-delete/<str:pk>/',
		}
	return Response(api_urls)
#@login_required(login_url='signin')
@api_view(['GET'])
def integranteList(request):
	integrantes = Integrante.objects.all().order_by('-id')
	serializer = IntegranteSerializer(integrantes, many=True)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['GET'])
def integranteDetail(request, pk):
	integrantes = Integrante.objects.get(id=pk)
	serializer = IntegranteSerializer(integrantes, many=False)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def integranteCreate(request):
	serializer = IntegranteSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def integranteUpdate(request, pk):
	integrante = Integrante.objects.get(id=pk)
	serializer = IntegranteSerializer(instance=integrante, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['DELETE'])
def integranteDelete(request, pk):
	integrante = Integrante.objects.get(id=pk)
	integrante.delete()
	return Response('Item integrante succsesfully delete!')
