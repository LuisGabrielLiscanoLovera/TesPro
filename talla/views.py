
from traceback import print_tb
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
from despacho.models import Despacho
from django.db.models import Sum, F 

# Create your views here.




    







@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/talla-list/',
        'List':'/tallaOP-list/',
  
		}
	return Response(api_urls)





#@login_required(login_url='signin')


#talla
@api_view(['GET'])  
def TallaList(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    lastEm     = CambioEmpres.objects.filter(usuario_id=idUser).last()
   
    
    cantalla   = Talla.objects.filter(empresa_id=lastEm.lastEm).order_by('-id')
    serializer = TallaSerializer(cantalla, many=True)
    
    return Response(serializer.data)


#can tallas de la op
@api_view(['GET'])  
def TallaOPList(request):
    if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)             
    lastEm   = CambioEmpres.objects.filter(usuario_id=idUser.id).last() 
    ptalla   = CanTalla.objects.filter(empresa_id=lastEm.lastEm,operacion_id=int(request.GET.get('idOp', None))).order_by('-id')
    serializer = CanTallaSerializer(ptalla, many=True)
    return Response(serializer.data)
 
 
#tallas generales TallaEmpresaList
@api_view(['GET'])  
def TallaEmpresaList(request):
    if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)
           
    lastEm   = CambioEmpres.objects.filter(usuario_id=idUser.id).last() 
    ptalla   = Talla.objects.filter(empresa_id=lastEm.lastEm).order_by('-id')
    
    serializer = TallaSerializer(ptalla, many=True)
   
    return Response(serializer.data)
 

 
@api_view(['GET'])  
def TallaOpCanIncosistente(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    lastEm        = CambioEmpres.objects.filter(usuario_id=idUser.id).last() 
    idOP          = request.GET.get('idOperacion', None) 
    CanOperacion  = Operacion.objects.filter(id=int(idOP)).values('can_total')
    CanOperacion  = CanOperacion[0]['can_total']
    
    CanTallaTotal   = CanTalla.objects.filter(empresa_id=lastEm.lastEm,operacion_id=idOP).aggregate(can_talla=Sum('can_talla'))
    CanTallaTotal   = CanTallaTotal['can_talla']
    TotalOpRestante = Operacion.objects.filter(id=idOP).values('can_restante','fecha_cierre') 
    FechaCierre     = TotalOpRestante[0]['fecha_cierre']
    
    TotalOpRestante = TotalOpRestante[0]['can_restante']
    
    data = {
        'CanTallaTotal':CanTallaTotal,
        'CanOperacion':CanOperacion,
        'TotalOpRestante':TotalOpRestante,
        'FechaCierre':FechaCierre
        }
    
   
    
    return JsonResponse(data)
 
 
 
 
 
 
 
 
 
 
 
 
 
#create talla 
class CreateTalla(View):
    def  get(self, request):
        if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)
    
        nomTalla           = request.GET.get('nomTalla', None).upper()
        numTalla           = int(request.GET.get('numTalla', None))
        #idEmpresaTalla     = int(request.GET.get('idEmpresaTalla', None))
        lastEm             = CambioEmpres.objects.filter(usuario_id=idUser.id).last()

        existeTallaUser    =  Talla.objects.extra(where=["nom_talla='%s' AND usuario_id = '%s' AND empresa_id = '%s'" %(nomTalla,idUser.id,lastEm.lastEm)])
        if existeTallaUser.count()==0:
                
            obj = Talla.objects.create(
              
                empresa_id   = lastEm.lastEm,
                usuario_id   = idUser.id,
                nom_talla    = nomTalla, 
                num_talla    = numTalla,                   
            )
            obj = Talla.objects.latest('id')
            obj = Talla.objects.all().filter(id=obj.id).update(btnAddTalla="<input type='number' style='background-color : #f5f2f2; '  class='form-control-sm input-group-number' name='inputTalla-{}'  id='inputTalla-{}'>".format(obj.id,obj.id))
            
            data = {
            'user': "user"
        }
        else:
            data = {
            'user': "enviar un mensaje de error talla repetida"
        }
            print("enviar un mensaje de error talla repetida")
        return JsonResponse(data)

#create talla op

class CreateTallaOP(View):
    def  get(self, request):       
        
        if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)                
        lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last() 
        
        cantTalla        = int(request.GET.get('cantTalla', None))
        idOperacionTalla = int(request.GET.get('idOperacionTalla', None))        
        #para usar 2 formularios en operacion agregando talla
        f2 = int(request.GET.get('f2', None))      
        if f2 == 2:     
            idTalla  = str(request.GET.get('idTallaOPP', None))            
            idTalla  = Talla.objects.filter(nom_talla = idTalla, empresa_id=lastEm.lastEm).values('id')
            ptalla   = CanTalla.objects.filter(empresa_id=lastEm.lastEm,talla_id=idTalla[0]['id'],operacion_id=idOperacionTalla)

           
        else:
            idTalla = int(request.GET.get('idTalla', None))
            ptalla  = CanTalla.objects.filter(empresa_id=lastEm.lastEm,talla_id=idTalla,operacion_id=idOperacionTalla)
        
        if int(ptalla.count()) <= 0 :
            obj = CanTalla.objects.create(
                empresa_id   = lastEm.lastEm,
                usuario_id   = idUser.id,
                can_talla    = cantTalla,
                res_talla    = cantTalla,
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
        #boorar en tabla despacho
        idOpCantalla = CanTalla.objects.filter(id=id1).values('id','operacion_id','talla_id')       
        Despacho.objects.filter(operacion_id=idOpCantalla[0]['operacion_id'],talla_id=idOpCantalla[0]['talla_id']).delete()
        #boorar en tabla CanTalla
        CanTalla.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        
        return JsonResponse(data)


class UpdateTalla(TemplateView):
    def  get(self, request):
        idIptalla        = request.GET.get('idIptallaUP', None)
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








