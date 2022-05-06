import json
from django.shortcuts import redirect
from tarea.models import Tarea
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils import (dateformat, formats)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TareaSerializer
from empresa.models import CambioEmpres
from authapp.models import MyUser

# Create your views here.




@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/tarea-list/'
		}
	return Response(api_urls)
#@login_required(login_url='signin')
from django.http import JsonResponse


@api_view(['GET'])
def TareaList(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    lastEm     = CambioEmpres.objects.filter(Usuario_id=idUser).last()
    lastEm=lastEm.lastEm
    tarea = Tarea.objects.all().filter(empresa_id=lastEm).order_by('-id')
    serializer = TareaSerializer(tarea, many=True)
    return Response(serializer.data)

    #return JsonResponse({'data':dt})
    #return JsonResponse({'data':serializer.data})
    
    #return jsonResponse()


class CreateTarea(View):
    

    def get(self, request):
        if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)
        
        lastEm           = CambioEmpres.objects.filter(Usuario_id=idUser.id).last()
      
        nombreTarea  = request.GET.get('nombreTarea', None).upper()
        minutoXTarea = int(request.GET.get('minutoXTarea', None))
        horaXTarea   = int(request.GET.get('horaXTarea', None))
        valorTarea   = int(request.GET.get('valorTarea', None))
        detalleTarea = request.GET.get('detalleTarea', None)
        
        
        
        try:
            obj = Tarea.objects.create(
                empresa_id = lastEm.lastEm,
                usuario_id = idUser.id,
                nom_tarea  = nombreTarea, 
                min_minuto = minutoXTarea, 
                min_hora   = horaXTarea,
                valor      = valorTarea,
                detalle    = detalleTarea,              
        )
  
            data = {
                'user': "Tarea creada"
        } 
           
            return JsonResponse(data)
        except Exception as e:
            data = {'user': "Error al crear tarea" }          
            return JsonResponse(data)




class DeleteTarea(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Tarea.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)




class UpdateTarea(TemplateView):
    def  get(self, request):
        nombreTarea 	 = request.GET.get('nombreTareaUP', None).upper()
        minutoXTarea	 = int(request.GET.get('minutoXTareaUP', None))
        horaXTarea  	 = int(request.GET.get('horaXTareaUP', None))
        valorTarea  	 = int(request.GET.get('valorTareaUP', None))
        detalleTarea	 = request.GET.get('detalleTareaUP', None)
        idempresaTarea 	 = int(request.GET.get('empresaTareaUP', None))
        idUserTarea      = int(request.GET.get('idUserTareaUP', None))
        idTareaUP        = int(request.GET.get('idTareaUP', None))
        
        obj = Tarea.objects.get(id=idTareaUP)
        obj.empresa_id = idempresaTarea
        obj.usuario_id = idUserTarea
        obj.nom_tarea  = nombreTarea  
        obj.min_minuto = minutoXTarea 
        obj.min_hora   = horaXTarea     
        obj.valor      = valorTarea
        obj.detalle    = detalleTarea  
        try:
            obj.save()
            return redirect('home')
        except Exception as e:  print(str(e),"reparar peo de cors header crsf token")












""" 
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
def TareaList(request):
	Tareas = Tarea.objects.all().order_by('-id')
	serializer = TareaSerializer(Tareas, many=True)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['GET'])
def TareaDetail(request, pk):
	Tareas = Tarea.objects.get(id=pk)
	serializer = TareaSerializer(Tareas, many=False)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def TareaCreate(request):
	serializer = TareaSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def TareaUpdate(request, pk):
	Tarea = Tarea.objects.get(id=pk)
	serializer = TareaSerializer(instance=Tarea, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['DELETE'])
def TareaDelete(request, pk):
	Tarea = Tarea.objects.get(id=pk)
	Tarea.delete()
	return Response('Item Tarea succsesfully delete!')
 """