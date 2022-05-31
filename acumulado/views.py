from django import views
import json
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from integrante.models import Integrante
from patinador.models import Patinador
from talla.models import Talla,CanTalla
from operacion.models import Operacion 
from django.db.models import Sum, F 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authapp.models import MyUser
from acumulado.models import Acumulado as ACUMULADO
from acumulado.models import ProAcumulado as  ProAcu
from tarea.models import Tarea
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import View
from django.http import JsonResponse, HttpResponse,Http404
from django.db.models import F
from acumulado.serializers import AcumuladoSerializer,AcuSerializerProc

class Acumulado(LoginRequiredMixin,TemplateView):     
     template_name = "pages/acumulado.html"
     success_url = '/'     
     def get_context_data(self, **kwargs):
          context = super(Acumulado, self).get_context_data(**kwargs)
          s = SessionStore()
          s['last_login'] = self.request.user.pk
          s.create()      
          
          AllEmpresa      = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])       
          lastEm          = CambioEmpres.objects.filter(usuario_id=s['last_login']).last()
          Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('id','nom_talla','num_talla')
          EmpresaActual   = Empresa.objects.filter(usuario=s['last_login'],id=int(lastEm.lastEm))
          Operaciones     = Operacion.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),estatus='A').values('nom_operacion','id')
          context = super(Acumulado, self).get_context_data(**kwargs)
          context['lastIdEmpresa']    = int(lastEm.lastEm) #ids empresas
          context['allTalla']         = Tallas             #todaslas las tallas
          context['allOperaciones']   = Operaciones        #todaslas operaciones 
          context['nomEmpresa']       = AllEmpresa         #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual      # nombre de la empresa actual
          context['last_login']       = s['last_login']    # ultimo inicio de seccion   
          try:
            patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('integrante_id')
            allPatinadores  = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),id=int(patinadores[0].get('integrante_id'))).values('nombres','apellidos','id')
            context['allPatinador']     = allPatinadores     #todos los patinadores de la empresa
            return context
          
          finally:
            return context
       





class AcumuladoHistorial(LoginRequiredMixin,TemplateView):     
     template_name = "pages/historial/acumuladoHistorial.html"
     success_url = '/'     
     def get_context_data(self, **kwargs):
          context = super(AcumuladoHistorial, self).get_context_data(**kwargs)
          s = SessionStore()
          s['last_login'] = self.request.user.pk
          s.create()      
          
          AllEmpresa      = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])       
          lastEm          = CambioEmpres.objects.filter(usuario_id=s['last_login']).last()
          Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('id','nom_talla','num_talla')
          EmpresaActual   = Empresa.objects.filter(usuario=s['last_login'],id=int(lastEm.lastEm))
          Operaciones     = Operacion.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),estatus='A').values('nom_operacion','id')
          context = super(AcumuladoHistorial, self).get_context_data(**kwargs)
          context['lastIdEmpresa']    = int(lastEm.lastEm) #ids empresas
          context['allTalla']         = Tallas             #todaslas las tallas
          context['allOperaciones']   = Operaciones        #todaslas operaciones 
          context['nomEmpresa']       = AllEmpresa         #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual      # nombre de la empresa actual
          context['last_login']       = s['last_login']    # ultimo inicio de seccion   
          try:
            patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('integrante_id')
            allPatinadores  = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),id=int(patinadores[0].get('integrante_id'))).values('nombres','apellidos','id')
            context['allPatinador']     = allPatinadores     #todos los patinadores de la empresa
            return context
          
          finally:
            return context
       

@api_view(['GET'])  
def AcumuladoListHistorial(request):
    if request.session.has_key('username'):
            if 'username' in request.session:
                username = request.session['username']
                idUser   = MyUser.objects.get(username = username)
    
    lastEm          = CambioEmpres.objects.filter(usuario_id = idUser.id).last()
    acumuladoQsect  = ACUMULADO.objects.filter(empresa_id = lastEm.lastEm,estatus='I').order_by('-id')
    AcumuladoSe     = AcumuladoSerializer(acumuladoQsect, many=True)   
    dump            = json.dumps(AcumuladoSe.data)   #dump serializer to json reponse 
    
    return HttpResponse(dump, content_type='application/json')




@api_view(['GET'])  
def AcumuladoListProc(request):
    if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username = username)    
    lastEm          = CambioEmpres.objects.filter(usuario_id=idUser).last()   
    idAcumulado     = request.GET.get('idAcumulado',None)
    
    acumuladoProc= ProAcu.objects.filter(usuario_id=idUser,empresa_id=lastEm.lastEm,acumulado_id=idAcumulado).order_by('-id')
    
    serializer = AcuSerializerProc(acumuladoProc, many=True)
    return Response(serializer.data)   
     
@api_view(['GET'])  
def AcumuladoList(request):
    if request.session.has_key('username'):
            if 'username' in request.session:
                username = request.session['username']
                idUser   = MyUser.objects.get(username = username)
    lastEm          = CambioEmpres.objects.filter(usuario_id = idUser.id).last()
    acumuladoQsect  = ACUMULADO.objects.filter(empresa_id = lastEm.lastEm,estatus='A').order_by('-id')
    AcumuladoSe     = AcumuladoSerializer(acumuladoQsect, many=True)   
    dump            = json.dumps(AcumuladoSe.data)   #dump serializer to json reponse 
    
    return HttpResponse(dump, content_type='application/json')
    
    
    
@api_view(['GET'])  
def AcumuladoListValor(request):
    if request.session.has_key('username'):
            if 'username' in request.session:
                username = request.session['username']
                idUser   = MyUser.objects.get(username = username)
    
    lastEm          = CambioEmpres.objects.filter(usuario_id = idUser.id).last()
    #acumuladoQsect  = ACUMULADO.objects.filter(empresa_id = lastEm.lastEm,estatus='A').order_by('-id')
    acumuladoQsect  = ACUMULADO.objects.filter(empresa_id = lastEm.lastEm).order_by('-id')
    
    AcumuladoSe     = AcumuladoSerializer(acumuladoQsect, many=True)   
    dump            = json.dumps(AcumuladoSe.data)   #dump serializer to json reponse 
    
    return HttpResponse(dump, content_type='application/json')
    
    
@api_view(['POST'])
def createAcumulado(request,):
    #Prod = Models AcumulcreateAcumulado
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
        
    lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last()  
   # canTerminada  = int(request.data['can_total_acu'])
    
    try: 
        obj = ACUMULADO.objects.create(
        usuario_id     = int(idUser.id),
        empresa_id     = int(lastEm.lastEm),
        nom_acumulado  = request.data['nom_acumulado'],
        nota           = request.data['nota_acu'],
       # can_total      = canTerminada,      
        )
                
        data = {            'Acumulado': "Acumulado guardado con exito!",
            'estatus':True
        }

    except Exception as e:
        data = { 'Acumulado': str(e),'estatus':False}        
        return Response("Acumulado no cargadA " +str(e) )
    return Response(data)
    
    
@api_view(['POST'])
def createProAcumulado(request,):

    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
        
    lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last()  
    canTerminada  = int(request.data['Cantidad_Acu'])
    
    
    try: 
        obj = ProAcu.objects.create(
        usuario_id     = int(idUser.id),
        empresa_id     = int(lastEm.lastEm),
        integrante_id  = int(request.data['OccionId_integrante_Acu']),
        patinador_id   = int(request.data['OccionId_pantinador_Acu']),
        tarea_id       = int(request.data['OccionId_tarea_Acu']),
        talla_id       = int(request.data['OccionId_talla_Acu']),
        can_prod_acum  = canTerminada,      
        acumulado_id    =int(request.data['acumulado_id'])
        )
                
        obj = ProAcu.objects.latest('id')
        btnDel="<button class='btn btn-block btn-sm btn-outline-danger icofont-ui-remove' type='submit' onclick='deleteAcumuladoUnico({})'> </button>".format(obj.id)
        obj = ProAcu.objects.all().filter(id=obj.id).update(delAcumulProc=btnDel)
        
        data = {
            'Acumulado': "Acumulado guardado con exito!",
            'estatus':True
        }
       
      

    except Exception as e:
        data = {'Acumulado': str(e),'estatus':False}        
        return Response(data)
    
    return Response(data)
    
   
@api_view(['GET'])
def AcumuladoDataIntegrante(request):
    if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username = username)    
    lastEm          = CambioEmpres.objects.filter(usuario_id=idUser).last()   
    idAcumulado     = request.GET.get('idAcumulado',None)    
    idIntegrante    = request.GET.get('idIntegranteSelect')   
    dontrepeYorself=[]
    tareas=[]
    patinadores=[]
    for tareasIntegrante in ProAcu.objects.filter(usuario_id=idUser,empresa_id=lastEm.lastEm,acumulado_id=int(idAcumulado), 
    integrante_id=idIntegrante).distinct().values('tarea_id','patinador_id'):       
        tareaIntegrante = (Tarea.objects.filter(usuario_id=idUser,empresa_id=lastEm.lastEm,id=tareasIntegrante['tarea_id']).values('nom_tarea','id')[0])  
        totalIntegrante = ProAcu.objects.filter(usuario_id=idUser,empresa_id=lastEm.lastEm,acumulado_id=int(idAcumulado),integrante_id=idIntegrante,tarea_id=tareaIntegrante['id']).values('tarea_id','can_prod_acum').aggregate(can_prod_acum=Sum('can_prod_acum'))
        patinador       = Patinador.objects.filter(usuario_id=idUser,empresa_id=lastEm.lastEm,id=tareasIntegrante['patinador_id']).distinct().values('integrante_id')
        patinador       = Integrante.objects.filter(usuario_id=idUser,empresa_id=lastEm.lastEm,id=patinador[0]['integrante_id']).values('nombres','apellidos')
        patinador       = "{} {}".format(patinador[0]['nombres'],patinador[0]['apellidos'] )
        
        if patinador in patinadores:pass
        else:patinadores.append(patinador)       
        if tareaIntegrante['nom_tarea'] in dontrepeYorself:pass
        else:           
            dontrepeYorself.append(tareaIntegrante['nom_tarea'])
            tareas.append({
            'tarea':tareaIntegrante['nom_tarea'],
            'cat_total_tarea':totalIntegrante['can_prod_acum'],
        })       
    if tareas==[]:pass
    else:
        if patinadores ==[]:pass 
        else:tareas.append({'patinadores':patinadores})
    return Response(tareas)




@api_view(['GET'])
def AcumuladoDataIntegranteValor(request):
    if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username = username)    
    lastEm          = CambioEmpres.objects.filter(usuario_id=idUser).last()   
    idAcumulado     = request.GET.get('idAcumulado',None)    
    idIntegrante    = request.GET.get('idIntegranteSelect')   
    
    totalGenerado=0
    dontrepeYorself=[]
    tareas=[]
    patinadores=[]    
    for tareasIntegrante in ProAcu.objects.filter(usuario_id=idUser,empresa_id=lastEm.lastEm,acumulado_id=int(idAcumulado), 
    integrante_id=idIntegrante).distinct().values('tarea_id','patinador_id'):       
        tareaIntegrante = (Tarea.objects.filter(usuario_id=idUser,empresa_id=lastEm.lastEm,id=tareasIntegrante['tarea_id']).values('nom_tarea','valor','id')[0])  
        totalIntegrante = ProAcu.objects.filter(usuario_id=idUser,empresa_id=lastEm.lastEm,acumulado_id=int(idAcumulado),integrante_id=idIntegrante,tarea_id=tareaIntegrante['id']).values('tarea_id','can_prod_acum').aggregate(can_prod_acum=Sum('can_prod_acum'))
        patinador       = Patinador.objects.filter(usuario_id=idUser,empresa_id=lastEm.lastEm,id=tareasIntegrante['patinador_id']).distinct().values('integrante_id')
        patinador       = Integrante.objects.filter(usuario_id=idUser,empresa_id=lastEm.lastEm,id=patinador[0]['integrante_id']).values('nombres','apellidos')
        patinador       = "{} {}".format(patinador[0]['nombres'],patinador[0]['apellidos'] )
        
        if patinador in patinadores:pass
        else:patinadores.append(patinador)
        
        
        if tareaIntegrante['nom_tarea'] in dontrepeYorself:pass
        else:           
            dontrepeYorself.append(tareaIntegrante['nom_tarea'])
            ValorTotalTarea=int(int(tareaIntegrante['valor']))*(int(totalIntegrante['can_prod_acum']))
            totalGenerado+=ValorTotalTarea            
            tareas.append({
            'tarea':tareaIntegrante['nom_tarea'],
            'cat_total_tarea':totalIntegrante['can_prod_acum'],
            'valorTarea':"$ {:0,.2f}".format(tareaIntegrante['valor']),            
            'ValorTotalTarea':"$ {:0,.2f}".format(ValorTotalTarea),
            'ValorTotalTarea':"$ {:0,.2f}".format(ValorTotalTarea),
           
        })       
    if tareas==[]:pass
    else:
        if patinadores ==[]:pass
        else:tareas.append({'patinadores':patinadores,'totalGenerado':"$ {:0,.2f}".format(totalGenerado)})
    
    return Response(tareas)

@api_view(['GET'])
def cerrarAcumulado(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)        
    lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
    idAcumulado=int(request.GET['idAcumulado'])    
    try:
        ACUMULADO.objects.filter(id=idAcumulado,empresa_id=lastEm.lastEm).update(estatus="I", fecha_cierre=( ACUMULADO.objects.filter(id=idAcumulado).values('updated_at')))
        ProAcu.objects.filter(casino_id=idAcumulado,empresa_id=lastEm.lastEm).update(estatus="I", fecha_cierre=( ACUMULADO.objects.filter(id=idAcumulado).values('updated_at')))
        data={"casino":True,"msj":"Acumulado cerrardo"}        
        return Response(data)
    except Exception as e:
        data={"casino":False,"msj":"Acumulado No cerrardo","error":str(e)}
        print(data)
        return Response(data)

@api_view(['GET'])
def abrirAcumulado(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)        
    lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
    idAcumulado=int(request.GET['idAcumuladoHistorial'])    
    try:
        ACUMULADO.objects.filter(id=idAcumulado,empresa_id=lastEm.lastEm).update(estatus="A", fecha_cierre=( ACUMULADO.objects.filter(id=idAcumulado).values('updated_at')))
        ProAcu.objects.filter(casino_id=idAcumulado,empresa_id=lastEm.lastEm).update(estatus="A", fecha_cierre=( ACUMULADO.objects.filter(id=idAcumulado).values('updated_at')))
        data={"casino":True,"msj":"Acumulado abierto"}        
        return Response(data)
    except Exception as e:
        data={"casino":False,"msj":"Acumulado No abierto","error":str(e)}
        print(data)
        return Response(data)





@api_view(['DELETE'])
def deleteAcumulado(request,id):
    try:
        ProAcu.objects.get(id=id).delete()
        data = {'deleted': True}
    except Exception as e:
        data = {
            'error':str(e),
            'deleted': False
        }
        Response(data)
    return JsonResponse(data)


class deleteAllAcumulado(View):
    def  get(self, request):
        idAcumulado = request.GET.get('id_acumulado', None)
        ACUMULADO.objects.get(id=idAcumulado).delete()
        data = {'deleted': True}
        return JsonResponse(data)

class ValorAcumulado(LoginRequiredMixin,TemplateView): 
     template_name = "pages/valorAcumulado.html"
     success_url = '/' 
     def get_context_data(self, **kwargs):
          context = super(ValorAcumulado, self).get_context_data(**kwargs)
          s = SessionStore()
          s['last_login'] = self.request.user.pk
          s.create()
          AllEmpresa      = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])       
          lastEm          = CambioEmpres.objects.filter(usuario_id=s['last_login']).last()
          Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('id','nom_talla','num_talla')
          EmpresaActual   = Empresa.objects.filter(usuario=s['last_login'],id=int(lastEm.lastEm))
          Operaciones     = Operacion.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),estatus='A').values('nom_operacion','id')
          context = super(ValorAcumulado, self).get_context_data(**kwargs)
          context['lastIdEmpresa']    = int(lastEm.lastEm) #ids empresas
          context['allTalla']         = Tallas             #todaslas las tallas
          context['allOperaciones']   = Operaciones        #todaslas operaciones 
          context['nomEmpresa']       = AllEmpresa         #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual      # nombre de la empresa actual
          context['last_login']       = s['last_login']    # ultimo inicio de seccion   
          try:
            patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm)).values('integrante_id')
            allPatinadores  = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm.lastEm),id=int(patinadores[0].get('integrante_id'))).values('nombres','apellidos','id')
            context['allPatinador']     = allPatinadores     #todos los patinadores de la empresa
            return context
          finally:
            return context

