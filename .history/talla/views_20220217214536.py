import json
from authapp.models import MyUser
from operacion.models import Operacion
from django.shortcuts import render, redirect
from integrante.models import Integrante
from talla.models import CanTalla, Talla
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils import (dateformat, formats)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TallaSerializer,CanTallaSerializer
from empresa.models import CambioEmpres
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.




    







@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/talla-list/',
        'List':'/tallaOP-list/',
  
		}
	return Response(api_urls)





#@login_required(login_url='signin')
from django.http import JsonResponse

#talla
@api_view(['GET'])  
def TallaList(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    lastEm     = CambioEmpres.objects.filter(Usuario_id=idUser).last()
    lastEm=lastEm.lastEm
    
    cantalla   = Talla.objects.filter(empresa_id=lastEm).order_by('-id')
    serializer = TallaSerializer(cantalla, many=True)
    
    return Response(serializer.data)
#can talla op
@api_view(['GET'])  
def TallaOPList(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
    
    
    lastEm     = CambioEmpres.objects.filter(Usuario_id=idUser).last()
    lastEm=lastEm.lastEm
    ptalla     = CanTalla.objects.filter(empresa_id=lastEm,operacion_id=int(request.GET.get('idOp', None))).order_by('-id')
    serializer = CanTallaSerializer(ptalla, many=True)
    return Response(serializer.data)
 
#create talla 
class CreateTalla(View):
    def  get(self, request):
        
        nomTalla           = request.GET.get('nomTalla', None).upper()
        
        
        #q = Talla.objects.filter(criterion1 & criterion2)
        Talla.objects.extra(where=["foo='a' OR bar = 'a'", "baz = 'a'"])

        ifNtallaExist      = Talla.objects.filter(nom_talla__contains=nomTalla)
        
        print(Talla,"gggggggg")
        
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

#create talla op

class CreateTallaOP(View):
    def  get(self, request):
        
        idTalla          = int(request.GET.get('idTalla', None))
        cantTalla        = int(request.GET.get('cantTalla', None))
        idOperacionTalla = int(request.GET.get('idOperacionTalla', None))
        idEmpresaOPTalla = int(request.GET.get('idEmpresaOPTalla', None))
        idUserOPTalla    = int(request.GET.get('idUserOPTalla', None))
        
        if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)
                
        
        lastEm     = CambioEmpres.objects.filter(Usuario_id=idUser).last()
        lastEm=lastEm.lastEm
        ptalla     = CanTalla.objects.filter(empresa_id=lastEm,talla_id=idTalla,operacion_id=idOperacionTalla)
        
        if int(ptalla.count()) <= 0 :
            obj = CanTalla.objects.create(
                empresa_id   = idEmpresaOPTalla,
                usuario_id   = idUserOPTalla,
                can_talla    = cantTalla, 
                talla_id     = idTalla, 
                operacion_id = idOperacionTalla
                
        )
  
            data = {
                'user': "user"
        } 
            return JsonResponse(data)
        else:
            print("NO pasoooo",ptalla.count())
            data = {'user': "user"} 
            return JsonResponse(data)










class DeleteTalla(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Talla.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class DeleteTallaOP(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CanTalla.objects.get(id=id1).delete()
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








