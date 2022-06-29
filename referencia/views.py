from django.shortcuts import redirect
from referencia.models import Referencia
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils import (dateformat, formats)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReferenciaSerializer
from empresa.models import CambioEmpres
from authapp.models import MyUser
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/referencia-list/'
		}
	return Response(api_urls)
#@login_required(login_url='signin')
@login_required(login_url='signin')
@api_view(['GET'])
def referenciaList(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    lastEm     = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
    lastEm=lastEm.lastEm
    referencias = Referencia.objects.all().filter(
    	empresa_id=lastEm, usuario_id=idUser.id,estatus='A').order_by('-id')
    
    
    serializer = ReferenciaSerializer(referencias, many=True)
    return Response(serializer.data)


class CreateReferencia(View):
    def  get(self, request):
        if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)
        
        
        lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
        nom_referencia = request.GET.get('nom_referencia', None).upper()
        descripcion    = request.GET.get('descripcion', None)
        #img1            = request.GET.get('img1', None)
        #img2            = request.GET.get('img2', None)
        
        #puede existir pero no repetido en la misma empresa
        existeReferecia =  Referencia.objects.extra(where=["nom_referencia='%s' AND usuario_id = '%s' AND empresa_id = '%s'" %(nom_referencia,idUser.id,lastEm.lastEm) ])
        
        if existeReferecia.count()==0:    
       # agregar empresa y usuario               
            obj = Referencia.objects.create(        
                nom_referencia = nom_referencia,
                descripcion    = descripcion,
                #fotoPrendaUno  = img1,
                #fotoPrendaDos  = img2,
                empresa_id     = lastEm.lastEm,
                usuario_id     = idUser.id,            
        )
            obj = Referencia.objects.latest('id')
            user = {'id':obj.id,'nom_referencia':obj.nom_referencia,'descripcion':obj.descripcion,'created_at':obj.created_at.strftime("%Y-%m-%d %H:%M:%S")}
            data = {
            'user': user,
             'estatus':True
        }
        else:
            data = {
            'user': "enviar un mensaje de error Referencia repetida repetido",
             'estatus':False
        }
            print("enviar un mensaje de error Referencia repetida ") 
        
        return JsonResponse(data)

class DeleteReferencia(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Referencia.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

''' 
class UpdateReferencia(TemplateView):
    def  get(self, request):
       
        idReferencia    = request.GET.get('idReferenciaUp', None)
        nom_referencia = request.GET.get('nom_referenciaUP', None)
        descripcion    = request.GET.get('descripcionUP', None)      
        idEmpresa       = request.GET.get('empresaUP', None)
        idUser          = request.GET.get('idUserUP', None)
        
        
        obj = Referencia.objects.get(id=idReferencia)
        obj.nom_referencia = nom_referencia
        obj.descripcion = descripcion
       
        obj.empresa_id = idEmpresa
        obj.usuario_id = idUser
        try:
            obj.save()
            return redirect('home')
        except Exception as e:
            print("reparar peo de cors header crsf token")
 '''

@api_view(['POST'])
def UpdateReferencia(request):
    idReferencia = request.data['idReferencia']    
    nom_referencia = request.data['nom_referenciaUP']
    descripcion = request.data['descripcionUP']   
    idUser = request.data['idUserUP']
    estatus = request.data['estatusUP']

    obj = Referencia.objects.get(id=idReferencia)
    obj.nom_referencia = nom_referencia
    obj.estatus     = estatus
    obj.descripcion = descripcion  
    obj.usuario_id = idUser
    
    
    try:
        obj.save()
        return redirect('home')
    except Exception as e:
        print("reparar peo de cors header crsf token")
    return Response(idReferencia)
