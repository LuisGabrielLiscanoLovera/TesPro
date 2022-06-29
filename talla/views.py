from authapp.models import MyUser
from operacion.models import Operacion
from django.shortcuts import redirect
from talla.models import CanTalla, Talla
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils import (dateformat, formats)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TallaSerializer,CanTallaSerializer
from empresa.models import CambioEmpres
from despacho.models import Despacho
from django.db.models import Sum, F 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.











@login_required(login_url='signin')
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/talla-list/',
        'List':'/tallaOP-list/',
  
		}
	return Response(api_urls)





#@login_required(login_url='signin')


#talla
@login_required(login_url='signin')
@api_view(['GET'])  
def TallaList(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username) 
    lastEm     = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
    cantalla = Talla.objects.filter(
    	empresa_id=lastEm.lastEm, usuario_id=idUser.id).order_by('-id')
    serializer = TallaSerializer(cantalla, many=True)
    return Response(serializer.data)


#can tallas de la op
@login_required(login_url='signin')
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
@login_required(login_url='signin')
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
 

 
@login_required(login_url='signin')
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
        idTalla = request.GET.get('id', None)
        sinTalla = Talla.objects.filter(id=idTalla).values('nom_talla')
        if (sinTalla[0]['nom_talla'] != 'SIN TALLA'):
            Talla.objects.get(id=idTalla).delete()
            data = {
            'deleted': True
            }
            return JsonResponse(data)
        else:
            
            data = {
                'deleted': False
            }
            return JsonResponse(data)


class DeleteTallaOP(View):
    def  get(self, request):
        idTalla = request.GET.get('id', None)
        idOpCantalla = CanTalla.objects.filter(id=idTalla).values('id','operacion_id','talla_id')       
        canT=0
          
        for canTerminada in Despacho.objects.filter(operacion_id=idOpCantalla[0]['operacion_id'],talla_id=idOpCantalla[0]['talla_id']).values('can_terminada'):canT+=canTerminada['can_terminada']
        Operacion.objects.all().filter(id=idOpCantalla[0]['operacion_id']).update(can_restante= F('can_restante') - int(canT))
        Despacho.objects.filter(operacion_id=idOpCantalla[0]['operacion_id'],talla_id=idOpCantalla[0]['talla_id']).delete()
        CanTalla.objects.get(id=idTalla).delete()
        data = {
            'deleted': True
        }        
        return JsonResponse(data)

class UpdateTalla(LoginRequiredMixin,TemplateView):
    def  get(self, request):
        idTalla        = request.GET.get('idTallaUP', None)
        idEmpresa      = request.GET.get('idEmpresaUP', None)
        idUser         = request.GET.get('idUserUP', None)
        estatus        = request.GET.get('estatusUP', None)
        nom_talla      = request.GET.get('nom_tallaUP', None)
        num_talla      = request.GET.get('num_tallaUP', None)
        sinTalla = Talla.objects.filter(
            id=idTalla).values('nom_talla')
        
        if (sinTalla[0]['nom_talla']!='SIN TALLA'):
            try:
                obj = Talla.objects.get(id=idTalla)
                obj.empresa_id = idEmpresa
                obj.usuario_id = idUser
                obj.estatus    = estatus  
                obj.num_talla  = num_talla
                obj.nom_talla  = nom_talla.upper()
                obj.save()
                return redirect('home')
            except Exception as e:
                print("reparar peo de cors header crsf token Error:"+str(e))
        else:
            return redirect('home')







