from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TareaSerializer
from django.contrib.auth.decorators import login_required
from .models import Tarea
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/Tarea-list/',
		'Detail View':'/Tarea-detail/<str:pk>/',
		'Create':'/Tarea-create/',
		'Update':'/Tarea-update/<str:pk>/',
		'Delete':'/Tarea-delete/<str:pk>/',
		}
	return Response(api_urls)
#@login_required(login_url='signin')
@api_view(['GET'])
def tareaList(request):
	tareas = Tarea.objects.all().order_by('-id')
	serializer = TareaSerializer(tareas, many=True)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['GET'])
def tareaDetail(request, pk):
	tareas = Tarea.objects.get(id=pk)
	serializer = TareaSerializer(tareas, many=False)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def tareaCreate(request):
	serializer = TareaSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def tareaUpdate(request, pk):
	tarea = Tarea.objects.get(id=pk)
	serializer = TareaSerializer(instance=tarea, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['DELETE'])
def tareaDelete(request, pk):
	tarea = Tarea.objects.get(id=pk)
	tarea.delete()
	return Response('Item tarea succsesfully delete!')
