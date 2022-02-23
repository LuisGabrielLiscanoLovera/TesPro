from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render, redirect

from operacion.models import Operacion
from authapp.models import MyUser
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils import (dateformat, formats)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OperacionSerializer
from empresa.models import CambioEmpres
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/operacion-list/'
		}
	return Response(api_urls)
#@login_required(login_url='signin')


@api_view(['GET'])  
def operacionList(request):
    #capturamos el inicio de session   
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    lastEm     = CambioEmpres.objects.filter(Usuario_id=idUser).last()
    operacion  = Operacion.objects.filter(empresa_id=lastEm.lastEm).order_by('-id')
    serializer = OperacionSerializer(operacion, many=True)
     
    return Response(serializer.data)


class CreateOperacion(View):
    
    def  get(self, request):
        can_totalOP    = request.GET.get('can_totalOP', None)
        idReferenciaOP = request.GET.get('idReferenciaOP', None)
        idEmpresaOP    = int(request.GET.get('idEmpresaOP', None))
        idColorOP      = int(request.GET.get('idColorOP', None))
        idUserOP       = int(request.GET.get('idUserOP', None))
        nomOperacion   = request.GET.get('nomOperacion', None)
        estatus = 'A'
        obj = Operacion.objects.create(
            empresa_id     = idEmpresaOP,
            usuario_id     = idUserOP,
            nom_operacion  = "OP"+nomOperacion, 
            estatus        = estatus,
            color_id       = idColorOP,
            referencia_id  = idReferenciaOP,
            can_total      = can_totalOP
          
              
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
        idIpoperacion    = request.GET.get('idIpoperacionUP', None)
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






