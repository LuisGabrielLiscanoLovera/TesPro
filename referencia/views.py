from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReferenciaSerializer
from django.contrib.auth.decorators import login_required
from .models import Referencia
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/Referencia-list/',
		'Detail View':'/Referencia-detail/<str:pk>/',
		'Create':'/Referencia-create/',
		'Update':'/Referencia-update/<str:pk>/',
		'Delete':'/Referencia-delete/<str:pk>/',
		}
	return Response(api_urls)
#@login_required(login_url='signin')
@api_view(['GET'])
def referenciaList(request):
	referencias = Referencia.objects.all().order_by('-id')
	serializer = ReferenciaSerializer(referencias, many=True)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['GET'])
def referenciaDetail(request, pk):
	referencias = Referencia.objects.get(id=pk)
	serializer = ReferenciaSerializer(referencias, many=False)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def referenciaCreate(request):
	request.data._mutable = True
	request.data._mutable = False
	serializer = ReferenciaSerializer(data=request.data)
	print(type(request.data))
	print((request.data))
	if serializer.is_valid():
		print(type(request.data))
		print((request.data))
		serializer.save()
	return Response(serializer.data)




#@login_required(login_url='signin')
@api_view(['POST'])
def referenciaUpdate(request, pk):
	referencia = Referencia.objects.get(id=pk)
	serializer = ReferenciaSerializer(instance=referencia, data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['DELETE'])
def referenciaDelete(request, pk):
	referencia = Referencia.objects.get(id=pk)
	referencia.delete()
	return Response('Item succsesfully delete!')
