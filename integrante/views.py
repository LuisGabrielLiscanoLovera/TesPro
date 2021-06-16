import json
from django.shortcuts import redirect
from integrante.models import Integrante
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils import (dateformat, formats)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import IntegranteSerializer
from empresa.models import CambioEmpres

# Create your views here.




@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/integrante-list/'
		}
	return Response(api_urls)
#@login_required(login_url='signin')
from django.http import JsonResponse


@api_view(['GET'])
def integranteList(request):
    lastEm=CambioEmpres.objects.values('lastEm').last().get("lastEm")
    integrante = Integrante.objects.all().filter(empresa_id=lastEm).order_by('-id')
    serializer = IntegranteSerializer(integrante, many=True)
    print(serializer.data)
    return Response(serializer.data)

    #return JsonResponse({'data':dt})
    #return JsonResponse({'data':serializer.data})
    
    #return jsonResponse()


class CreateIntegrante(View):
    def  get(self, request):       
        idEmpresa        = request.GET.get('idEmpresa', None)
        idUser           = request.GET.get('idUser', None)
        nombres          = request.GET.get('nomIntegrante', None)
        apellido         = request.GET.get('apeIntegrante', None)
        sexo             = request.GET.get('sexo', None)
        estatus          = request.GET.get('estatus', None)
        correo           = request.GET.get('correo', None)
        cedula           = request.GET.get('cedula', None)
        num_telf         = request.GET.get('num_telefono', None)
        direccion        = request.GET.get('direccion', None)
        abilidad         = request.GET.get('abilidad', None)
  
        print("idEmpresa:      >>>>",idEmpresa,idUser)
        obj = Integrante.objects.create(
            empresa_id  = idEmpresa,
            usuario_id  = idUser,
            nombres     = nombres, 
            apellido    = apellido, 
            sexo        = sexo, 
            estatus     = estatus, 
            correo      = correo, 
            cedula      = cedula, 
            num_telf    = num_telf, 
            direccion   = direccion, 
            abilidad    = abilidad, 
              
        )
  
        data = {
            'user': "user"
        } 
        return JsonResponse(data)

class DeleteIntegrante(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Integrante.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)




class UpdateIntegrante(TemplateView):
    def  get(self, request):        
        
        idEmpresa        = request.GET.get('empresaUP', None)
        idUser           = request.GET.get('idUserUP', None)
        idIntegrante     = request.GET.get('idIntegranteUP', None)
        nombres          = request.GET.get('nomIntegranteUP', None)
        apellido         = request.GET.get('apeIntegranteUP', None)
        sexo             = request.GET.get('sexoUP', None)
        estatus          = request.GET.get('estatusUP', None)
        correo           = request.GET.get('correoUP', None)
        cedula           = request.GET.get('cedulaUP', None)
        num_telf         = request.GET.get('num_telefonoUP', None)
        direccion        = request.GET.get('direccionUP', None)
        abilidad         = request.GET.get('abilidadUP', None)
        
        obj = Integrante.objects.get(id=idIntegrante)
        obj.empresa_id = idEmpresa
        obj.usuario_id = idUser
        obj.nombres    = nombres  
        obj.apellido   = apellido 
        obj.sexo       = sexo     
        obj.estatus    = estatus  
        obj.correo     = correo   
        obj.cedula     = cedula   
        obj.num_telf   = num_telf 
        obj.direccion  = direccion
        obj.abilidad   = abilidad 

        
        try:
            obj.save()
            return redirect('home')
        except Exception as e:  print("reparar peo de cors header crsf token")












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
 """