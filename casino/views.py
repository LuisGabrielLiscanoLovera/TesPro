import json
from casino.models import Casino, Importe
from integrante.models import Integrante
from patinador.models import Patinador
from django.contrib.sessions.backends.db import SessionStore
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authapp.models import MyUser
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from casino.serializers import CasinoSerializer,ImporteSerializer
from django.db.models import Sum, F 

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/Casino-list/',
	    'List':'/casinoImporte-list/',
		}
	return Response(api_urls)
	
@api_view(['GET'])
def casinoList(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)

    lastEm     = CambioEmpres.objects.filter(usuario_id=idUser).last()
    lastEm     = lastEm.lastEm
    casinos    = Casino.objects.filter(empresa_id=lastEm,usuario_id=idUser,estatus='A').order_by('-id')
    serializer = CasinoSerializer(casinos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createCasino(request,):
    #Prod = Models AcumulcreateCasino
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
        
    lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
    
    try: 
        obj = Casino.objects.create(
        usuario_id     = int(idUser.id),
        empresa_id     = int(lastEm.lastEm),
        nom_casino     = request.data['nom_casino'],
        
        )
                
        data = {'Casino': "Casino guardado con exito!",
                'estatus':True}
    except Exception as e:
        data = { 'Error': str(e),'estatus':False}        
        return Response("Casino no cargadA " +str(e) )
    return Response(data)
    
    
    
    
    
@api_view(['GET'])
def CasinoDataIntegranteImporte(request):
    if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username = username)    
    lastEm          = CambioEmpres.objects.filter(usuario_id=idUser).last()   
    idCasino     = request.GET.get('idCasino',None)    
    idIntegrante    = request.GET.get('idIntegranteSelect')    
       
    importeCasino=Importe.objects.filter(usuario_id=idUser,empresa_id=lastEm.lastEm,casino_id=int(idCasino),
    integrante_id=idIntegrante)

    serializer = ImporteSerializer(importeCasino, many=True)
    return Response(serializer.data)
    
    

    
    