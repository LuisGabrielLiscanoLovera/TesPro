from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ColorSerializer
from django.contrib.auth.decorators import login_required
from .models import Color
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/Color-list/',
		'Detail View':'/Color-detail/<str:pk>/',
		'Create':'/Color-create/',
		'Update':'/Color-update/<str:pk>/',
		'Delete':'/Color-delete/<str:pk>/',
		}
	return Response(api_urls)
#@login_required(login_url='signin')
@api_view(['GET'])
def colorList(request):
	colors = Color.objects.all().order_by('-id')
	serializer = ColorSerializer(colors, many=True)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['GET'])
def colorDetail(request, pk):
	colors = Color.objects.get(id=pk)
	serializer = ColorSerializer(colors, many=False)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def colorCreate(request):
	serializer = ColorSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def colorUpdate(request, pk):
	color = Color.objects.get(id=pk)
	serializer = ColorSerializer(instance=color, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['DELETE'])
def colorDelete(request, pk):
	color = Color.objects.get(id=pk)
	color.delete()
	return Response('Item color succsesfully delete!')
