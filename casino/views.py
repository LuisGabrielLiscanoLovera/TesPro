from django.shortcuts import redirect
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CasinoSerializer,ImporteSerializer
from django.contrib.auth.decorators import login_required
from .models import Casino, Importe
from empresa.models import CambioEmpres
from django.views.generic import View
import re
from django.views.generic.base import TemplateView
from authapp.models import MyUser

class CasinoTemplate(TemplateView):
     template_name = "pages/casino.html"

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/Casino-list/',
	    'List':'/casinoImporte-list/',
		}
	return Response(api_urls)
#@login_required(login_url='signin')
@api_view(['GET'])
def casinoList(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    lastEm     = CambioEmpres.objects.filter(usuario_id=idUser).last()
    lastEm=lastEm.lastEm
    casinos = Casino.objects.filter(empresa_id=lastEm).order_by('-id')
    serializer = CasinoSerializer(casinos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def casinoListImporte(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    lastEm     = CambioEmpres.objects.filter(usuario_id=idUser).last()
    
    idCasinoImporte=int(request.GET.get('idCasinoImporte', None))
    casinos = Importe.objects.filter(empresa_id=lastEm.lastEm,casino_id=idCasinoImporte).order_by('-id')
    serializer = ImporteSerializer(casinos, many=True)
    return Response(serializer.data)


class CreateCasino(View):
    
    def  get(self, request):
        if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)
        
        lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
        idIntegrante     = int(request.GET.get('idIntegranteCasino', None))
        print(lastEm,idIntegrante,idUser)

        try:
            Casino.objects.create(
            empresa_id   = lastEm.lastEm,
            usuario_id   = idUser.id,
            integrante_id= idIntegrante, 
            )
  
            data = {
            'casino': True
        }
        
        except Exception as e:
            data = {
            'casino': False
        }
            print("reparar peo de cors header crsf token")
        return JsonResponse(data)


class UpdateCasino(TemplateView):
    def  get(self, request):

        idCasino     = request.GET.get('idCasino', None)
        idEmpresa    = request.GET.get('idEmpresaUPCasino', None)
        idUser       = request.GET.get('idUserUPCasino', None)
        deuda        = request.GET.get('importes',None)
        idIntegranteImporte = int(request.GET.get('idIntegranteImporte', None))
        
        lasDeuda=Casino.objects.filter(id=idCasino).values_list('deuda', flat=True)
        lasDeuda=re.sub("[^0-9]","",str(lasDeuda))     
        
        obj = Importe.objects.create(
            cantidad      = deuda,          
            empresa_id    = idEmpresa,
            casino_id     = idCasino
              
        )
        obj = Casino.objects.get(id=idCasino)
        obj.empresa_id = idEmpresa
        obj.usuario_id = idUser
        obj.cantidad   = deuda      
        obj.deuda      = int(deuda)+int(lasDeuda)
        
        

        
        try:
            obj.save()
            return redirect('home')
        except Exception as e:  print("reparar peo de cors header crsf token")



"""#@login_required(login_url='signin')
@api_view(['GET'])
def casinoDetail(request, pk):
	casinos = Casino.objects.get(id=pk)
	serializer = CasinoSerializer(casinos, many=False)
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def casinoCreate(request):
	serializer = CasinoSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['POST'])
def casinoUpdate(request, pk):
	casino = Casino.objects.get(id=pk)
	serializer = CasinoSerializer(instance=casino, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#@login_required(login_url='signin')
@api_view(['DELETE'])
def casinoDelete(request, pk):
	casino = Casino.objects.get(id=pk)
	casino.delete()
	return Response('Item casino succsesfully delete!')
"""
