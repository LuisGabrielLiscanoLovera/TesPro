import json
from django.shortcuts import render, redirect
from patinador.forms import PatinadorCreationForm
from integrante.models import Integrante
from patinador.models import Patinador
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils import (dateformat, formats)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PatinadorSerializer
from empresa.models import CambioEmpres
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from authapp.models import MyUser


# Create your views here.




    







@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/patinador-list/'
		}
	return Response(api_urls)
#@login_required(login_url='signin')
from django.http import JsonResponse


@api_view(['GET'])  
def patinadorList(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    lastEm     = CambioEmpres.objects.filter(Usuario_id=idUser).last()
    patinador  = Patinador.objects.filter(empresa_id=lastEm.lastEm).order_by('-id')
    serializer = PatinadorSerializer(patinador, many=True)
    
    return Response(serializer.data)


class CreatePatinador(View):
    
    
    def  get(self, request):
        if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)
        
        lastEm              = CambioEmpres.objects.filter(Usuario_id=idUser.id).last()
        #idEmpresa          = request.GET.get('idEmpresa', None)
        idIntegrante        = int(request.GET.get('idIntegrante', None))
        estatus             = 'A'
        ctrlDespachoCheck   = request.GET.get('ctrlDespacho', None)
        
        #check box al agregar patinador para el control del despacho 
        if (ctrlDespachoCheck=='true'):ctrlDespachoCheck=1
        elif (ctrlDespachoCheck=='false'):ctrlDespachoCheck=0
        
        #puede existir pero no repetido en la misma empresa
        existeIntPat    =  Patinador.objects.extra(where=["integrante_id='%s' AND usuario_id = '%s' AND empresa_id = '%s'" %(idIntegrante,idUser.id,lastEm.lastEm) ])
       
               
        if existeIntPat.count()==0:
          
            obj = Patinador.objects.create(
                empresa_id   = lastEm.lastEm,
                usuario_id   = idUser.id,
                integrante_id= idIntegrante, 
                estatus      = estatus,
                ctrlDespacho = ctrlDespachoCheck,
            ) 
           
            data = {
            'user': "user"
        }
        
        else:
            data = {
            'user': "enviar un mensaje de error patinador repetido"
        }
            print("enviar un mensaje de error patinador repetida") 
        
        return JsonResponse(data)

class DeletePatinador(View):
    def  get(self, request):
        id1 = request.GET.get('idPatinador', None)
        print(id1,6666666666666666666)
        Patinador.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)




class UpdatePatinador(TemplateView):
    def  get(self, request):
        idIpatinador     = request.GET.get('idIpatinadorUP', None)
        idEmpresa        = request.GET.get('idEmpresaUP', None)
        idUser           = request.GET.get('idUserUP', None)
        nombres          = request.GET.get('nombresInputUP', None)
        apellido         = request.GET.get('apellidosUP', None)
        sexo             = request.GET.get('sexoUP', None)
        estatus          = request.GET.get('estatusUP', None)
        correo           = request.GET.get('correoUP', None)
        cedula           = request.GET.get('cedulaUP', None)
        num_telf         = request.GET.get('num_telefonoUP', None)
        direccion        = request.GET.get('direccionUP', None)
        abilidad         = request.GET.get('abilidadUP', None)
        
      
        obj = Patinador.objects.get(id=idIpatinador)
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
		'List':'/Patinador-list/',
		'Detail View':'/Patinador-detail/<str:pk>/',
		'Create':'/Patinador-create/',
		'Update':'/Patinador-update/<str:pk>/',
		'Delete':'/Patinador-delete/<str:pk>/',
		}
	return Response(api_urls)
#@login_required(login_url='signin')
@api_view(['GET'])
def patinadorList(request):
	patinadores = Patinador.objects.all().order_by('-id')
	serializer = PatinadorSerializer(patinadores, many=True)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['GET'])
def patinadorDetail(request, pk):
	patinadores = Patinador.objects.get(id=pk)
	serializer = PatinadorSerializer(patinadores, many=False)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def patinadorCreate(request):
	serializer = PatinadorSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def patinadorUpdate(request, pk):
	patinador = Patinador.objects.get(id=pk)
	serializer = PatinadorSerializer(instance=patinador, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['DELETE'])
def patinadorDelete(request, pk):
	patinador = Patinador.objects.get(id=pk)
	patinador.delete()
	return Response('Item patinador succsesfully delete!')
"""
