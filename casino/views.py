from ast import Import
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
from patinador.serializers import PatinadorSerializer


@api_view(['POST'])
def createProCasino(request,):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
        
    lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last()  
    canTerminada  = int(request.data['Cantidad_Casino'])
    try: 
        obj = Importe.objects.create(
        usuario_id     = int(idUser.id),
        empresa_id     = int(lastEm.lastEm),
        integrante_id  = int(request.data['OccionId_integrante_Casino']),
        patinador_id   = int(request.data['OccionId_pantinador_Casino']),        
        cantidad       = canTerminada,      
        casino_id      = int(request.data['idCasino'])
        )
        Casino.objects.all().filter(id=int(request.data['idCasino'])).update(can_total=F('can_total') + canTerminada)  
        obj = Importe.objects.latest('id')
        btnDel="<button class='btn btn-block btn-sm btn-outline-danger icofont-ui-remove' type='submit' onclick='deleteImporteUnico({})'> </button>".format(obj.id)
        obj = Importe.objects.all().filter(id=obj.id).update(delCasinoImport=btnDel)
        
        data = {
            'Acumulado': "Casino guardado con exito!",
            'estatus':True
        }  

    except Exception as e:
        data = {'Errror': str(e),'estatus':False}        
        return Response(data)
    
    return Response(data)   
    

@api_view(['DELETE'])
def deleteImporteUnico(request,id):
    try:
        canTerminada =  Importe.objects.filter(id=id).values('cantidad','casino_id')
        Casino.objects.filter(id=canTerminada[0]['casino_id']).update(can_total= F('can_total') - canTerminada[0]['cantidad'])
        
        Importe.objects.get(id=id).delete()
        data = {'deleted': True}        
    except Exception as e:           
        data = {
            'error':str(e),
            'deleted': False      
        }        
        Response(data)
    return JsonResponse(data)
@api_view(['GET'])
def CasinoDataImporte(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
    lastEm        = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
    idCasino      = request.GET.get('idCasino', None)
    importeGeneral=Importe.objects.filter(usuario_id=int(idUser.id),casino_id=idCasino,empresa_id=lastEm.lastEm).order_by("-id")
    serializer = ImporteSerializer(importeGeneral, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TotalImporteInte(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)    
    lastEm             = CambioEmpres.objects.filter(usuario_id=idUser.id).last()    
    idCasino           = request.GET.get('idCasino', None)  
    idIntegranteSelect = request.GET.get('idIntegranteSelect', None)   
    casinoImporte      = Importe.objects.filter(empresa_id=lastEm.lastEm,
    usuario_id = idUser.id, integrante_id=idIntegranteSelect,casino_id=int(idCasino)).aggregate(cantidad=Sum('cantidad'))
    cedula             = Integrante.objects.filter(id=idIntegranteSelect,empresa_id=lastEm.lastEm,usuario_id=idUser.id ).distinct().values('cedula')
    cedula = cedula[0]['cedula']
    TotalCasinoImporte = casinoImporte['cantidad']
    data = {'TotalCasinoImporte':TotalCasinoImporte,'cedulaIntegrante':cedula}  
    return JsonResponse(data)

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
    
    

    
@api_view(['GET'])  
def patinadoresActCasino(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)            
    lastEm = CambioEmpres.objects.filter(usuario_id=idUser).last()
    lastEm = lastEm.lastEm    
    try:        
        patinadores     = Patinador.objects.all().filter(usuario=idUser,estatus='A' ,ctrlCasino=1 ,empresa_id=int(lastEm))
        serializer      = PatinadorSerializer(patinadores, many=True)        
        return Response(serializer.data)
    except Exception as e:    
        data={'error':str(e),'msj':"no tienes patinadores activos"}
        return Response(data)
        