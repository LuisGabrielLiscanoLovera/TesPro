from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CasinoSerializer
from django.contrib.auth.decorators import login_required
from .models import Casino

from django.views.generic.base import TemplateView
class CasinoTemplate(TemplateView):
     template_name = "pages/casino.html"

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/Casino-list/',
		'Detail View':'/Casino-detail/<str:pk>/',
		'Create':'/Casino-create/',
		'Update':'/Casino-update/<str:pk>/',
		'Delete':'/Casino-delete/<str:pk>/',
		}
	return Response(api_urls)
#@login_required(login_url='signin')
@api_view(['GET'])
def casinoList(request):
	casinos = Casino.objects.all().order_by('-id')
	serializer = CasinoSerializer(casinos, many=True)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['GET'])
def casinoDetail(request, pk):
	casinos = Casino.objects.get(id=pk)
	serializer = CasinoSerializer(casinos, many=False)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def casinoCreate(request):
	serializer = CasinoSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def casinoUpdate(request, pk):
	casino = Casino.objects.get(id=pk)
	serializer = CasinoSerializer(instance=casino, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['DELETE'])
def casinoDelete(request, pk):
	casino = Casino.objects.get(id=pk)
	casino.delete()
	return Response('Item casino succsesfully delete!')
