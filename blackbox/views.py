import json
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django import views
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect, render
from empresa.models import Empresa,RelacionEmpresa,CambioEmpres
from despacho.models import Despacho
from casino.models import Casino
from tarea.models import Tarea
from casino.serializers import CasinoSerializer
from acumulado.models import Acumulado as ACUMULADO
from integrante.models import Integrante
from patinador.models import Patinador
from produccion.models import Produccion as Prod
from talla.models import Talla,CanTalla
from django.db.models import Sum, F 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authapp.models import MyUser
from despacho.serializers import DespachoSerializer,OperacionSerializer
from acumulado.serializers import AcumuladoSerializer
from integrante.serializers import IntegranteSerializer
from patinador.serializers import PatinadorSerializer
from tarea.serializers import TareaSerializer
from produccion.serializers import ProduccionSerializer
from talla.serializers import TallaSerializer,CanTallaSerializer
from operacion.models import Operacion
from django.views.generic import View
from django.http import JsonResponse, Http404, HttpResponse
from django.db.models import F
from django_serverside_datatable.views import ServerSideDatatableView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

    
@api_view(['GET'])  
def operacionesListPatinadores(request):     
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
    
    lastEm=Integrante.objects.filter(id=idUser.id).values('empresa_id')
    lastEm=int(lastEm[0]['empresa_id'])
    #vamos bien
    despacho   = Operacion.objects.filter(empresa_id=lastEm,estatus='A').order_by('-id')
    serializer = OperacionSerializer(despacho, many=True)
    
    return Response(serializer.data)
  

class DespachoPatinador(LoginRequiredMixin,TemplateView):
     
     template_name = "pages/despachoPerfilPatinador.html"
     success_url = '/'     
     def get_context_data(self, **kwargs):
          context = super(DespachoPatinador, self).get_context_data(**kwargs)
          s = SessionStore()
          s['last_login'] = self.request.user.pk
          s.create()
          lastEm=Integrante.objects.filter(id=s['last_login']).values('empresa_id')
          lastEm=int(lastEm[0]['empresa_id'])
          
          AllEmpresa      = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])          
         # Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=lastEm).values('id','nom_talla','num_talla')
          EmpresaActual   = Empresa.objects.filter(usuario=s['last_login'],id=int(lastEm))
          Operaciones     = Operacion.objects.filter(usuario=s['last_login'],empresa_id=lastEm,estatus='A').values('nom_operacion','id')
          context = super(DespachoPatinador, self).get_context_data(**kwargs)
          context['login_user_id']    = s['last_login']   # aqui se obtiene el user id
          context['lastIdEmpresa']    = int(lastEm) # ids empresas
          #context['allTalla']         = Tallas             #todaslas las tallas
          context['allOperaciones']   = Operaciones        #todaslas operaciones 
          context['nomEmpresa']       = AllEmpresa         #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual      # nombre de la empresa actual
          context['last_login']       = s['last_login']    # ultimo inicio de seccion
          try:
              patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=lastEm).values('integrante_id')
              allPatinadores  = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=lastEm,id=int(patinadores[0].get('integrante_id'))).values('nombres','apellidos','id')
              context['allPatinador']     = allPatinadores     #todos los patinadores de la empresa
              return context
          finally:
            return context  
    
@api_view(['POST'])
def createDespachoPatinador(request,):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
        
    
    integranteConten=Integrante.objects.filter(id=idUser.id).values('empresa_id','usuario_id')
    lastEm=int(integranteConten[0]['empresa_id'])   
    canTerminada  = int(request.data['cantPatinador'])
    
    #nombreTalla   = Talla.objects.filter(empresa_id=int(lastEm),usuario_id=int(idUser.id)     ,id=int(request.data['selectIdTalla'])).values('nom_talla')
                                                                                                                                       
    nombreTalla   = Talla.objects.filter(empresa_id=int(lastEm),usuario_id=int(integranteConten[0]['usuario_id']),id=int(request.data['selectIdTallaPatinador'])).values('nom_talla','id')
    idPatinador   = Patinador.objects.filter(integrante_id=idUser.id).values('id')
    idPatinador  = idPatinador[0]['id']
    
  
    
    
    nomPatinador  = Integrante.objects.filter(empresa_id=int(lastEm),usuario_id=int(integranteConten[0]['usuario_id']) ,id=int(idUser.id)).values('nombres','apellidos')
    nom_patinador = nomPatinador[0]['nombres']+" "+nomPatinador[0]['apellidos']
  
    try:
        obj = Despacho.objects.create(
        usuario_id           = int(integranteConten[0]['usuario_id']),
        patinador_id         = idPatinador,
        empresa_id           = int(lastEm),
        operacion_id         = int(request.data['id_OPPatinador']), 
        talla_id             = nombreTalla[0]['id'],
        can_terminada        = canTerminada,
        nomTallaDespacho     = nombreTalla[0]['nom_talla'],
        nomPatinadorDespacho = nom_patinador

        )
        obj = Despacho.objects.latest('id')
        btnDel="<button class='btn btn-block btn-sm btn-outline-danger icofont-ui-remove' type='submit' onclick='deleteDespachoUnico({})'> </button>".format(obj.id)
        obj = Despacho.objects.all().filter(id=obj.id).update(btnDelDespacho=btnDel)
        data = {'despacho': True}
        CanTallaOP      = CanTalla.objects.all().filter(operacion_id=int(request.data['id_OPPatinador']),talla_id=int(request.data['selectIdTallaPatinador'])).update(res_talla= F('res_talla') - canTerminada)
        OpTallaRestante = Operacion.objects.all().filter(id=int(request.data['id_OPPatinador'])).update(can_restante= F('can_restante') - canTerminada)
        return Response(data)
    except Exception as e:
        print(str(e))
        data={'msj':'despacho no cargado','error':str(e)}
        return Response(data)

class ItemListViewPatinador(ServerSideDatatableView):  
    columns = ['nomPatinadorDespacho','nomTallaDespacho','can_terminada','created_at','btnDelDespacho','id']
    
    def get_queryset(self):
        if self.request.method == 'GET':           
            idOp = self.request.GET.get('idOpPatinador', None)
            idUser = self.request.GET.get('usuarioPatinador', None)
            #integranteConten=Integrante.objects.filter(id=idUser.id).values('empresa_id','usuario_id')

            
            if idOp and idUser is not None:
                lastEm=Integrante.objects.filter(id=idUser).values('empresa_id')
                lastEm=int(lastEm[0]['empresa_id'])               
                queryset   = Despacho.objects.filter(empresa_id=int(lastEm),operacion_id=idOp).order_by('-id')          
            return queryset
    
@api_view(['GET'])  
def TallaOPListPatinador(request):
    if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)             
    lastEm=Integrante.objects.filter(id=idUser.id).values('empresa_id')
    lastEm=int(lastEm[0]['empresa_id'])
    ptalla   = CanTalla.objects.filter(empresa_id=lastEm,operacion_id=int(request.GET.get('idOp', None))).order_by('-id')
    serializer = CanTallaSerializer(ptalla, many=True)
    return Response(serializer.data)
 

@api_view(['GET'])  
def TallaOpCanIncosistentePatinadores(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    
    
    
    
    lastEm        = CambioEmpres.objects.filter(usuario_id=idUser.id).last() 
    idOP          = request.GET.get('idOperacion', None) 
    CanOperacion  = Operacion.objects.filter(id=int(idOP)).values('can_total')
    CanOperacion  = CanOperacion[0]['can_total']    
    CanTallaTotal   = CanTalla.objects.filter(empresa_id=lastEm,operacion_id=idOP).aggregate(can_talla=Sum('can_talla'))
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
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
class ProduccionPatinador(LoginRequiredMixin,TemplateView):
     template_name = "pages/produccionPerfilPatinador.html"     
     success_url = '/'
     
     def get_context_data(self, **kwargs):
          context = super(ProduccionPatinador, self).get_context_data(**kwargs)

          s = SessionStore()
          s['last_login'] = self.request.user.pk
          s.create()
          
          lastEm=Integrante.objects.filter(id=s['last_login']).values('empresa_id')
          lastEm=int(lastEm[0]['empresa_id'])
          
          
          
          AllEmpresa      = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])       
          #lastEm          = CambioEmpres.objects.filter(usuario_id=s['last_login']).last()
          #Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm)).values('id','nom_talla','num_talla')
          EmpresaActual   = Empresa.objects.filter(usuario=s['last_login'],id=int(lastEm))
          Operaciones     = Operacion.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm),estatus='A').values('nom_operacion','id')
          context = super(ProduccionPatinador, self).get_context_data(**kwargs)
          context['login_user_id']    = s['last_login']   # aqui se obtiene el user id
          context['lastIdEmpresa']    = int(lastEm) # ids empresas
          #context['allTalla']         = Tallas             #todaslas las tallas
          context['allOperaciones']   = Operaciones        #todaslas operaciones 
          context['nomEmpresa']       = AllEmpresa         #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual      # nombre de la empresa actual
          context['last_login']       = s['last_login']    # ultimo inicio de seccion

          try:
            patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm)).values('integrante_id')
            allPatinadores  = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm),id=int(patinadores[0].get('integrante_id'))).values('nombres','apellidos','id')
            context['allPatinador']     = allPatinadores     #todos los patinadores de la empresa
            return context
          finally:
            return context        

@api_view(['GET'])  
def produccionesListPatinadores(request):     
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
    
    lastEm=Integrante.objects.filter(id=idUser.id).values('empresa_id')
    lastEm=int(lastEm[0]['empresa_id'])
    #vamos bien
    despacho   = Operacion.objects.filter(empresa_id=lastEm,estatus='A').order_by('-id')
    serializer = OperacionSerializer(despacho, many=True)
    
    return Response(serializer.data)



#dataProduccionInte-list/
@api_view(['GET'])
def ProduccionDataIntegrantePatinador(request):
    if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username = username)    
    
    lastEm=Integrante.objects.filter(id=idUser.id).values('empresa_id')
    lastEm=int(lastEm[0]['empresa_id'])
    
    idOperacion     = request.GET.get('idOpPatinador',None)    
    idIntegrante    = request.GET.get('idIntegranteSelectPatinador')
    dontrepeYorself = []
    tareas = []
    patinadores = []   
    for tareasIntegrante in Prod.objects.filter(empresa_id=lastEm,operacion_id=int(idOperacion),integrante_id=idIntegrante).distinct().values('tarea_id','patinador_id'):
        tareaIntegrante = (Tarea.objects.filter(empresa_id=lastEm,id=tareasIntegrante['tarea_id']).values('nom_tarea','id')[0])  
        totalIntegrante = Prod.objects.filter(empresa_id=lastEm,operacion_id=int(idOperacion),integrante_id=idIntegrante,tarea_id=tareaIntegrante['id']).values('tarea_id','can_terminada').aggregate(can_terminada=Sum('can_terminada'))
        patinador       = Patinador.objects.filter(empresa_id=lastEm,id=tareasIntegrante['patinador_id']).distinct().values('integrante_id')
        patinador       = Integrante.objects.filter(empresa_id=lastEm,id=patinador[0]['integrante_id']).values('nombres','apellidos')
        patinador       = "{} {}".format(patinador[0]['nombres'],patinador[0]['apellidos'] ) 
        if patinador in patinadores:pass
        else:patinadores.append(patinador)
        if tareaIntegrante['nom_tarea'] in dontrepeYorself:pass
        else:           
            dontrepeYorself.append(tareaIntegrante['nom_tarea'])
            tareas.append({
            'tarea':tareaIntegrante['nom_tarea'],
            'cat_total_tarea':totalIntegrante['can_terminada'],
        })       
    if tareas==[]:pass
    else:
        if patinadores ==[]:pass 
        else:tareas.append({'patinadores':patinadores})
    return Response(tareas)
  
  
@api_view(['GET'])
def TareaListPatinador(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
    
    lastEm=Integrante.objects.filter(id=idUser.id).values('empresa_id')
    lastEm=int(lastEm[0]['empresa_id'])
    
    
   
    tarea = Tarea.objects.all().filter(empresa_id=lastEm,estatus='A').order_by('-id')
    serializer = TareaSerializer(tarea, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def integranteListPatinador(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
  
  
  
  
    lastEm=Integrante.objects.filter(id=idUser.id).values('empresa_id')
    lastEm=int(lastEm[0]['empresa_id'])  
    
    
    
    integrante = Integrante.objects.all().filter(empresa_id=lastEm,estatus='A').order_by('-id')
    try:
        serializer = IntegranteSerializer(integrante, many=True)
        return Response(serializer.data)
    except Exception as e:    
        print(str(e),"no tienes patinadores activos")   
        return Response("no tienes patinadores activos")








@api_view(['GET'])  
def patinadoresActProdPatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)            
    lastEm=Integrante.objects.filter(id=idUser.id).values('empresa_id')
    lastEm=int(lastEm[0]['empresa_id'])  
    try:        
        patinadores     = Patinador.objects.all().filter(usuario=idUser,estatus='A',ctrlProduccion=1, empresa_id=int(lastEm))
        serializer      = PatinadorSerializer(patinadores, many=True)        
        return Response(serializer.data)
    except Exception as e:    
        print(str(e),"no tienes patinadores activos")   
        return Response("no tienes patinadores activos")
        
        
        
     




@api_view(['POST'])
def createProduccionPatinador(request,):
    #Prod = Models Produccion
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
        
    integranteConten=Integrante.objects.filter(id=idUser.id).values('empresa_id','usuario_id')
    lastEm=int(integranteConten[0]['empresa_id'])
    idPatinador   = Patinador.objects.filter(integrante_id=idUser.id).values('id')
    idPatinador  = idPatinador[0]['id']
    
    
    
    canTerminada  = int(request.data['cantidadProdPatinador'])
    
    try: 
        obj = Prod.objects.create(
        usuario_id           = int(integranteConten[0]['usuario_id']),
        patinador_id         = idPatinador,
        
        
        
        integrante_id        = int(request.data['OccionId_integrante_prodPatinador']),
        empresa_id           = int(lastEm),
        operacion_id         = int(request.data['idOperacionPatinador']),
        talla_id             = int(request.data['OccionId_tallaPatinador']),
        tarea_id             = int(request.data['OccionId_tareaPatinador']),
        can_terminada        = canTerminada       
        )
        
        
        
        
        
        obj = Prod.objects.latest('id')
        btnDel="<button class='btn btn-block btn-sm btn-outline-danger icofont-ui-remove' type='submit' onclick='deleteProduccionUnico({})'> </button>".format(obj.id)
        obj = Prod.objects.all().filter(id=obj.id).update(delProduccion=btnDel)
        data = {
            'produccion': "Produccion guardado con exito!",
            'estatus':True
        }
       
        return Response(data)

    except Exception as e:
        print(str(e))
        return Response("PRODUCCION no cargadA " +str(e) )
   
  











class AcumuladoPatinador(LoginRequiredMixin,TemplateView):     
     template_name = "pages/acumuladoPerfilPatinador.html"
     success_url = '/'     
     def get_context_data(self, **kwargs):
          context = super(AcumuladoPatinador, self).get_context_data(**kwargs)
          s = SessionStore()
          s['last_login'] = self.request.user.pk
          s.create()        
          lastEm=Integrante.objects.filter(id=s['last_login']).values('empresa_id')
          lastEm=int(lastEm[0]['empresa_id'])
          AllEmpresa      = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])       
          EmpresaActual   = Empresa.objects.filter(usuario=s['last_login'],id=int(lastEm))
          context = super(AcumuladoPatinador, self).get_context_data(**kwargs)
          context['lastIdEmpresa']    = int(lastEm) #ids empresas
          context['nomEmpresa']       = AllEmpresa         #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual      # nombre de la empresa actual
          context['last_login']       = s['last_login']    # ultimo inicio de seccion   
          try:
            patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm)).values('integrante_id')
            allPatinadores  = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm),id=int(patinadores[0].get('integrante_id'))).values('nombres','apellidos','id')
            context['allPatinador']     = allPatinadores     #todos los patinadores de la empresa
            return context          
          finally:
            return context
       
@api_view(['GET'])  
def AcumuladoListPatinadores(request):
    if request.session.has_key('username'):
            if 'username' in request.session:
                username = request.session['username']
                idUse.idr   = MyUser.objects.get(username = username)
    
 
    lastEm=Integrante.objects.filter(id=idUse.idr.id).values('empresa_id')
    lastEm=int(lastEm[0]['empresa_id'])  
    acumuladoQsect  = ACUMULADO.objects.filter(empresa_id = lastEm,estatus='A').order_by('-id')
    AcumuladoSe     = AcumuladoSerializer(acumuladoQsect, many=True)   
    dump            = json.dumps(AcumuladoSe.data)   #dump serializer to json reponse 
    
    return HttpResponse(dump, content_type='application/json')
    
    




class CasinoHomePatinador(LoginRequiredMixin,TemplateView):
     template_name = "pages/casinoActivoPerfilPatinador.html"
     success_url = '/'
     def get_context_data(self, **kwargs):
          context = super(CasinoHomePatinador, self).get_context_data(**kwargs)
          s = SessionStore()
          s['last_login'] = self.request.user.pk
          s.create()
          AllEmpresa      = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])       
          
          lastEm=Integrante.objects.filter(id=s['last_login']).values('empresa_id')
          lastEm=int(lastEm[0]['empresa_id'])
          
          Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm)).values('id','nom_talla','num_talla')
          EmpresaActual   = Empresa.objects.filter(usuario=s['last_login'],id=int(lastEm))
          Operaciones     = Operacion.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm),estatus='A').values('nom_operacion','id')
          context = super(CasinoHomePatinador, self).get_context_data(**kwargs)
          context['login_user_id']    = s['last_login']   # aqui se obtiene el user id
          context['lastIdEmpresa']    = int(lastEm) #ids empresas
          context['allTalla']         = Tallas             #todaslas las tallas
          context['allOperaciones']   = Operaciones        #todaslas operaciones 
          context['nomEmpresa']       = AllEmpresa         #nombre de todas las empresa
          context['nomEmpresaU']      = EmpresaActual      # nombre de la empresa actual
          context['last_login']       = s['last_login']    # ultimo inicio de seccion   
          try:
            patinadores     = Patinador.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm)).values('integrante_id')
            allPatinadores  = Integrante.objects.all().filter(usuario=s['last_login'],empresa_id=int(lastEm),id=int(patinadores[0].get('integrante_id'))).values('nombres','apellidos','id')
            context['allPatinador']     = allPatinadores     #todos los patinadores de la empresa
            return context
          finally:
            return context





@api_view(['GET'])
def casinoListPatinador(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)   
    
    
    lastEm=Integrante.objects.filter(id=idUser.id).values('empresa_id')
    lastEm=int(lastEm[0]['empresa_id'])
    
    casinos    = Casino.objects.filter(empresa_id=lastEm,estatus='A').order_by('-id')
    serializer = CasinoSerializer(casinos, many=True)
    return Response(serializer.data)
 
 
 
 
@api_view(['GET'])  
def ProduccionOPListPatinador(request):
    if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username = username)
    
    lastEm=Integrante.objects.filter(id=idUser.id).values('empresa_id')
    lastEm=int(lastEm[0]['empresa_id'])            
    
    produccion = Prod.objects.filter(empresa_id = lastEm,operacion_id=int(request.GET.get('idOp', None))).order_by('-id')
    ProduccionSe = ProduccionSerializer(produccion, many=True)   
    dump = json.dumps(ProduccionSe.data)   #dump serializer to json reponse 
    
 
    return HttpResponse(dump, content_type='application/json')
    
    