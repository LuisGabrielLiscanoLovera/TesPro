# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PrendaSerializer
from django.contrib.auth.decorators import login_required
from .models import Prenda
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/Prenda-list/',
		'Detail View':'/Prenda-detail/<str:pk>/',
		'Create':'/Prenda-create/',
		'Update':'/Prenda-update/<str:pk>/',
		'Delete':'/Prenda-delete/<str:pk>/',
		}
	return Response(api_urls)
#@login_required(login_url='signin')
@api_view(['GET'])
def prendaList(request):
	prendas = Prenda.objects.all().order_by('-id')
	serializer = PrendaSerializer(prendas, many=True)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['GET'])
def prendaDetail(request, pk):
	prendas = Prenda.objects.get(id=pk)
	serializer = PrendaSerializer(prendas, many=False)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def prendaCreate(request):
	serializer = PrendaSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def prendaUpdate(request, pk):
	prenda = Prenda.objects.get(id=pk)
	serializer = PrendaSerializer(instance=prenda, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['DELETE'])
def prendaDelete(request, pk):
	prenda = Prenda.objects.get(id=pk)
	prenda.delete()
	return Response('Item prenda succsesfully delete!')
