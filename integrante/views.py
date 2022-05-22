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
from authapp.models import MyUser

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
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)

    lastEm     = CambioEmpres.objects.filter(usuario_id=idUser).last()    
    integrante = Integrante.objects.all().filter(empresa_id=lastEm.lastEm,estatus='A').order_by('-id')
    serializer = IntegranteSerializer(integrante, many=True)
    return Response(serializer.data)

    #return JsonResponse({'data':dt})
    #return JsonResponse({'data':serializer.data})
    
    #return jsonResponse()


class CreateIntegrante(View):
    
    
    def  get(self, request):
        if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)
        
        lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
        nombres          = request.GET.get('nomIntegrante', None).upper()
        apellido         = request.GET.get('apeIntegrante', None).upper()
        sexo             = request.GET.get('genero', None)
        correo           = request.GET.get('correo', None)
        cedula           = request.GET.get('cedula', None)
        num_telf         = request.GET.get('num_telefono', None)
        direccion        = request.GET.get('direccion', None).upper()
        estatus          = ('A')
        
        #puede existir pero no repetido en la misma empresa
        existeIntegrante =  Integrante.objects.extra(where=["cedula = '%s' AND usuario_id = '%s' AND empresa_id = '%s'" %(cedula,idUser.id,lastEm.lastEm) ])

        if existeIntegrante.count()==0:
    
        
            obj = Integrante.objects.create(
                empresa_id   = lastEm.lastEm,
                usuario_id   = idUser.id,
                nombres      = nombres, 
                apellidos    = apellido, 
                sexo         = sexo,
                estatus      = estatus,
                correo       = correo, 
                cedula       = cedula, 
                num_telf     = num_telf, 
                direccion    = direccion, 
              
        )
  
            data = {
            'user': "user",
             'estatus':True
        }
        else:
            data = {
            'user': "enviar un mensaje de error Integrante repetido",
            'estatus':False
        }
            print("enviar un mensaje de error Integrante repetidao") 
        
        
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
        
        idIntegrante     = request.GET.get('idIntegranteUP', None)
        idEmpresa        = request.GET.get('idEmpresaUP', None)
        idUser           = request.GET.get('idUserUP', None)
        nombres          = request.GET.get('nombresInputUP', None).upper()
        apellido         = request.GET.get('apellidosUP', None).upper()
        sexo             = request.GET.get('generoUP', None)
        estatus          = request.GET.get('estatusUP', None)
        correo           = request.GET.get('correoUP', None)
        cedula           = request.GET.get('cedulaUP', None)
        num_telf         = request.GET.get('num_telefonoUP', None)
        direccion        = request.GET.get('direccionUP', None).upper()
        
      
        obj = Integrante.objects.get(id=idIntegrante)
        obj.empresa_id = idEmpresa
        obj.usuario_id = idUser
        obj.nombres    = nombres  
        obj.apellidos  = apellido 
        obj.sexo       = sexo     
        obj.estatus    = estatus  
        obj.correo     = correo   
        obj.cedula     = cedula   
        obj.num_telf   = num_telf 
        obj.direccion  = direccion
        
        

        
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