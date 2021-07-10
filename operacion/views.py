from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render, redirect
from integrante.models import Integrante
from operacion.models import Operacion
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils import (dateformat, formats)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from empresa.models import CambioEmpres
from django.shortcuts import render
from django.template.loader import render_to_string


# Create your views here.




    







@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/poperacion-list/'
		}
	return Response(api_urls)
#@login_required(login_url='signin')


@api_view(['GET'])  
def operacionList(request):
    lastEm=CambioEmpres.objects.values('lastEm').last().get("lastEm")
    operacion  = Operacion.objects.filter(empresa_id=lastEm).order_by('-id')
    serializer = OperacionSerializer(operacion, many=True)
    
    return Response(serializer.data)


class CreateOperacion(View):
    
    def  get(self, request):
        idEmpresa        = request.GET.get('idEmpresa', None)
        idUser           = request.GET.get('idUser', None)
        idIntegrante     = int(request.GET.get('idIntegrante', None))
        estatus          = 'A'
        print("integrante",idIntegrante)     
        obj = Operacion.objects.create(
            empresa_id   = idEmpresa,
            usuario_id   = idUser,
            integrante_id= idIntegrante, 
            estatus      = estatus, 
          
              
        )
  
        data = {
            'user': "user"
        } 
        return JsonResponse(data)

class DeleteOperacion(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Operacion.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)




class UpdateOperacion(TemplateView):
    def  get(self, request):
        idIpoperacion     = request.GET.get('idIpoperacionUP', None)
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
        
      
        obj = Operacion.objects.get(id=idIpoperacion)
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






