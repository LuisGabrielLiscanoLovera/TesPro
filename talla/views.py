import json
from django.shortcuts import render, redirect
from integrante.models import Integrante
from talla.models import Talla
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils import (dateformat, formats)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TallaSerializer
from empresa.models import CambioEmpres
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.




    







@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/talla-list/'
		}
	return Response(api_urls)
#@login_required(login_url='signin')
from django.http import JsonResponse


@api_view(['GET'])  
def TallaList(request):
    lastEm     = CambioEmpres.objects.values('lastEm').last().get("lastEm")
    ptalla     = Talla.objects.filter(empresa_id=lastEm).order_by('-id')
    serializer = TallaSerializer(ptalla, many=True)
    
    return Response(serializer.data)
 
 
class CreateTalla(View):
    def  get(self, request):
        
        nomTalla           = request.GET.get('nomTalla', None).upper()
        numTalla           = int(request.GET.get('numTalla', None))
        idEmpresaTalla     = int(request.GET.get('idEmpresaTalla', None))
        idUserTalla        = int(request.GET.get('idUserTalla', None))
        obj = Talla.objects.create(
            empresa_id   = idEmpresaTalla,
            usuario_id   = idUserTalla,
            nom_talla    = nomTalla, 
            num_talla    = numTalla, 
          
              
        )
  
        data = {
            'user': "user"
        } 
        return JsonResponse(data)

class DeleteTalla(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Talla.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)




class UpdateTalla(TemplateView):
    def  get(self, request):
        idIptalla     = request.GET.get('idIptallaUP', None)
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
        
      
        obj = Talla.objects.get(id=idIptalla)
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








