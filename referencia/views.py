from django.shortcuts import redirect
from referencia.models import Referencia
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils import (dateformat, formats)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReferenciaSerializer
from empresa.models import CambioEmpres

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/referencia-list/'
		}
	return Response(api_urls)
#@login_required(login_url='signin')
@api_view(['GET'])
def referenciaList(request):
    lastEm=CambioEmpres.objects.values('lastEm').last().get("lastEm")
    referencias = Referencia.objects.all().filter(empresa_id=lastEm).order_by('-id')
    
    
    serializer = ReferenciaSerializer(referencias, many=True)
    return Response(serializer.data)


class CreateReferencia(View):
    def  get(self, request):
        
        nom_referencia1 = request.GET.get('nom_referencia', None).upper()
        descripcion1    = request.GET.get('descripcion', None)
        img1            = request.GET.get('img1', None)
        img2            = request.GET.get('img2', None)
        idEmpresa       = request.GET.get('empresa', None)
        idUser          = request.GET.get('idUser', None)
       # agregar empresa y usuario
        print("idEmpresa:      >>>>",idEmpresa,idUser)
        obj = Referencia.objects.create(
            
            nom_referencia = nom_referencia1,
            descripcion    = descripcion1,
            fotoPrendaUno  = img1,
            fotoPrendaDos  = img2,
            empresa_id     = idEmpresa,
            usuario_id     = idUser,            
        )
        obj = Referencia.objects.latest('id')

        


        user = {'id':obj.id,'nom_referencia':obj.nom_referencia,'descripcion':obj.descripcion,'created_at':obj.created_at.strftime("%Y-%m-%d %H:%M:%S")}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteReferencia(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Referencia.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateReferencia(TemplateView):
    def  get(self, request):        
        idReferencia    = request.GET.get('idReferencia', None)
        nom_referencia2 = request.GET.get('nom_referenciaUP', None)
        descripcion2    = request.GET.get('descripcionUP', None)
        img1            = request.GET.get('img1UP', None)
        img2            = request.GET.get('img2UP', None)
        idEmpresa       = request.GET.get('empresaUP', None)
        idUser          = request.GET.get('idUserUP', None)
        obj = Referencia.objects.get(id=idReferencia)
        obj.nom_referencia = nom_referencia2
        obj.descripcion = descripcion2
        obj.img1 = img1
        obj.img2 = img2
        obj.empresa_id = idEmpresa
        obj.usuario_id = idUser
        try:
            obj.save()
            return redirect('home')
        except Exception as e:  print("reparar peo de cors header crsf token")






