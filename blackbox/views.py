import json
#from turtle import speed
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.backends.db import SessionStore
from empresa.models import Empresa, RelacionEmpresa, CambioEmpres
from despacho.models import Despacho
from casino.models import Casino, Importe
from tarea.models import Tarea
from casino.serializers import CasinoSerializer, ImporteSerializer
from acumulado.models import Acumulado as ACUMULADO
from integrante.models import Integrante
from patinador.models import Patinador
from produccion.models import Produccion as Prod
from talla.models import Talla, CanTalla
from django.db.models import Sum, F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authapp.models import MyUser
from despacho.serializers import OperacionSerializer
from acumulado.serializers import AcumuladoSerializer, AcuSerializerProc
from acumulado.serializers import AcumuladoSerializer
from integrante.serializers import IntegranteSerializer
from patinador.serializers import PatinadorSerializer
from tarea.serializers import TareaSerializer
from produccion.serializers import ProduccionSerializer
from talla.serializers import TallaSerializer, CanTallaSerializer
from operacion.models import Operacion
from django.http import JsonResponse, HttpResponse
from django_serverside_datatable.views import ServerSideDatatableView
from django.contrib.auth.mixins import LoginRequiredMixin
from acumulado.models import Acumulado as ACUMULADO
from acumulado.models import ProAcumulado as ProAcu
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
@api_view(['GET'])
def operacionesListPatinadores(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']

            idUser = MyUser.objects.get(username=username)

    lastEm = Integrante.objects.filter(id=idUser.integrante_id).values('empresa_id')
    lastEm = int(lastEm[0]['empresa_id'])
    #vamos bien
    despacho = Operacion.objects.filter(
        empresa_id=lastEm, estatus='A').order_by('-id')
    serializer = OperacionSerializer(despacho, many=True)

    return Response(serializer.data)


class DespachoPatinador(LoginRequiredMixin, TemplateView):
    template_name = "pages/blackbox/despachoPerfilPatinador.html"
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(DespachoPatinador, self).get_context_data(**kwargs)
        s = SessionStore()
        s['last_login'] = self.request.user.pk
        s.create()
        
        myuser = MyUser.objects.get(id=s['last_login'])
        integranteConten = Integrante.objects.filter(
            id=myuser.integrante_id).values('empresa_id', 'usuario_id')
        
        
        
        
        
        lastEm = int(integranteConten[0]['empresa_id'])
        AllEmpresa = RelacionEmpresa.objects.filter(
            usuario_id=int(integranteConten[0]['usuario_id']))

        # Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=lastEm).values('id','nom_talla','num_talla')
        EmpresaActual = Empresa.objects.filter(
            usuario=int(integranteConten[0]['usuario_id']), id=int(lastEm))
          
        Operaciones = Operacion.objects.filter(usuario=int(integranteConten[0]['usuario_id']), id=int(
            lastEm), empresa_id=lastEm, estatus='A').values('nom_operacion', 'id')
        context = super(DespachoPatinador, self).get_context_data(**kwargs)
        # aqui se obtiene el user id
        context['login_user_id'] = s['last_login']
        context['lastIdEmpresa'] = int(lastEm)  # ids empresas
         #context['allTalla']         = Tallas             #todaslas las tallas
        context['allOperaciones'] = Operaciones  # todaslas operaciones
        context['nomEmpresa'] = AllEmpresa  # nombre de todas las empresa
          # nombre de la empresa actual
        context['nomEmpresaU'] = EmpresaActual
        context['last_login'] = s['last_login']    # ultimo inicio de seccion
        
        try:
            patinadores = Patinador.objects.all().filter(usuario=int(integranteConten[0]['usuario_id']), id=int(lastEm), empresa_id=lastEm).values('integrante_id')
            allPatinadores = Integrante.objects.all().filter(usuario=int(integranteConten[0]['usuario_id']), empresa_id=lastEm, id=int(
            patinadores[0].get('integrante_id'))).values('nombres', 'apellidos', 'id')
              # todos los patinadores de la empresa
            context['allPatinador'] = allPatinadores
            return context
        finally:
            return context

@login_required(login_url='signin')
@api_view(['POST'])
def createDespachoPatinador(request,):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)
    integranteConten = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id', 'usuario_id')
    lastEm = int(integranteConten[0]['empresa_id'])
    
    
    canTerminada = int(request.data['cantPatinador'])
    nombreTalla = Talla.objects.filter(empresa_id=int(lastEm), usuario_id=int(
        integranteConten[0]['usuario_id']), id=int(request.data['selectIdTallaPatinador'])).values('nom_talla', 'id')
    
    idIntegranteMyuser = MyUser.objects.get(username=idUser.username)
    
    idPatinador = Patinador.objects.filter(
        integrante_id=idIntegranteMyuser.integrante_id).values('id')
    idPatinador = idPatinador[0]['id']    
    nomPatinador = Integrante.objects.filter(empresa_id=int(lastEm), usuario_id=int(
        integranteConten[0]['usuario_id']), id=int(idUser.integrante_id)).values('nombres', 'apellidos')
    nom_patinador = nomPatinador[0]['nombres']+" "+nomPatinador[0]['apellidos']
    
    try:
        obj = Despacho.objects.create(
            usuario_id=int(integranteConten[0]['usuario_id']),
            patinador_id=idPatinador,
            empresa_id=int(lastEm),
            operacion_id=int(request.data['id_OPPatinador']),
            talla_id=nombreTalla[0]['id'],
            can_terminada=canTerminada,
            nomTallaDespacho=nombreTalla[0]['nom_talla'],
            nomPatinadorDespacho=nom_patinador
        )
        obj = Despacho.objects.latest('id')
        btnDel = "<button class='btn btn-block btn-sm btn-outline-danger icofont-ui-remove' type='submit' onclick='deleteDespachoUnico({})'> </button>".format(
            obj.id)
        obj = Despacho.objects.all().filter(id=obj.id).update(btnDelDespacho=btnDel)
        data = {'despacho': True}
        CanTallaOP = CanTalla.objects.all().filter(operacion_id=int(request.data['id_OPPatinador']), talla_id=int(
            request.data['selectIdTallaPatinador'])).update(res_talla=F('res_talla') - canTerminada)
        OpTallaRestante = Operacion.objects.all().filter(id=int(
            request.data['id_OPPatinador'])).update(can_restante=F('can_restante') - canTerminada)
        return Response(data)
    except Exception as e:
        print(str(e))
        data = {'msj': 'despacho no cargado', 'error': str(e)}
        return Response(data)


class ItemListViewPatinador(ServerSideDatatableView):
    columns = ['nomPatinadorDespacho', 'nomTallaDespacho',
               'can_terminada', 'created_at', 'btnDelDespacho', 'id']

    def get_queryset(self):
        if self.request.session.has_key('username'):
            if 'username' in self.request.session:
                username = self.request.session['username']
                idUser = MyUser.objects.get(username=username)
        lastEm = Integrante.objects.filter(id=idUser.integrante_id).values('empresa_id')
        lastEm = int(lastEm[0]['empresa_id'])
        
        if self.request.method == 'GET':
            idOp = self.request.GET.get('idOpPatinador', None)
            usuarioPatinador = self.request.GET.get('usuarioPatinador', None)
            queryset = Despacho.objects.filter(empresa_id=lastEm, operacion_id=idOp).order_by('-id')
            return queryset

@login_required(login_url='signin')
@api_view(['GET'])
def TallaOPListPatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)
    lastEm = Integrante.objects.filter(id=idUser.integrante_id).values('empresa_id')
    lastEm = int(lastEm[0]['empresa_id'])
    ptalla = CanTalla.objects.filter(empresa_id=lastEm, operacion_id=int(
        request.GET.get('idOp', None))).order_by('-id')
    serializer = CanTallaSerializer(ptalla, many=True)
    return Response(serializer.data)

@login_required(login_url='signin')
@api_view(['GET'])
def TallaOpCanIncosistentePatinadores(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = CambioEmpres.objects.filter(
        usuario_id=idUser.integrante_id).last()
    idOP = request.GET.get('idOperacion', None)
    CanOperacion = Operacion.objects.filter(id=int(idOP)).values('can_total')
    CanOperacion = CanOperacion[0]['can_total']
    CanTallaTotal = CanTalla.objects.filter(
        empresa_id=lastEm, operacion_id=idOP).aggregate(can_talla=Sum('can_talla'))
    CanTallaTotal = CanTallaTotal['can_talla']
    TotalOpRestante = Operacion.objects.filter(
        id=idOP).values('can_restante', 'fecha_cierre')
    FechaCierre = TotalOpRestante[0]['fecha_cierre']
    TotalOpRestante = TotalOpRestante[0]['can_restante']

    data = {
        'CanTallaTotal': CanTallaTotal,
        'CanOperacion': CanOperacion,
        'TotalOpRestante': TotalOpRestante,
        'FechaCierre': FechaCierre
    }

    return JsonResponse(data)


class ProduccionPatinador(LoginRequiredMixin, TemplateView):
    template_name = "pages/blackbox/produccionPerfilPatinador.html"
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ProduccionPatinador, self).get_context_data(**kwargs)
        s = SessionStore()
        s['last_login'] = self.request.user.pk
        s.create()
        integranteConten = Integrante.objects.filter(
            id=s['last_login']).values('empresa_id', 'usuario_id')

        lastEm = int(integranteConten[0]['empresa_id'])

        AllEmpresa = RelacionEmpresa.objects.filter(
            usuario_id=int(integranteConten[0]['usuario_id']))
        #lastEm          = CambioEmpres.objects.filter(usuario_id=s['last_login']).last()
        #Tallas          = Talla.objects.filter(usuario=s['last_login'],empresa_id=int(lastEm)).values('id','nom_talla','num_talla')
        EmpresaActual = Empresa.objects.filter(usuario=int(
            integranteConten[0]['usuario_id']), id=int(lastEm))
        Operaciones = Operacion.objects.filter(usuario=int(integranteConten[0]['usuario_id']), empresa_id=int(
            lastEm), estatus='A').values('nom_operacion', 'id')
        context = super(ProduccionPatinador, self).get_context_data(**kwargs)
        # aqui se obtiene el user id
        context['login_user_id'] = s['last_login']
        context['lastIdEmpresa'] = int(lastEm)  # ids empresas
        #context['allTalla']         = Tallas             #todaslas las tallas
        context['allOperaciones'] = Operaciones  # todaslas operaciones
        context['nomEmpresa'] = AllEmpresa  # nombre de todas las empresa
          # nombre de la empresa actual
        context['nomEmpresaU'] = EmpresaActual
        context['last_login'] = s['last_login']    # ultimo inicio de seccion

        try:
            patinadores = Patinador.objects.all().filter(usuario=int(
                integranteConten[0]['usuario_id']), empresa_id=int(lastEm)).values('integrante_id')
            allPatinadores = Integrante.objects.all().filter(usuario=int(integranteConten[0]['usuario_id']), empresa_id=int(
                lastEm), id=int(patinadores[0].get('integrante_id'))).values('nombres', 'apellidos', 'id')
            # todos los patinadores de la empresa
            context['allPatinador'] = allPatinadores
            return context
        finally:
            return context

@login_required(login_url='signin')
@api_view(['GET'])
def produccionesListPatinadores(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id')
    lastEm = int(lastEm[0]['empresa_id'])
    #vamos bien
    despacho = Operacion.objects.filter(
        empresa_id=lastEm, estatus='A').order_by('-id')
    serializer = OperacionSerializer(despacho, many=True)

    return Response(serializer.data)


@login_required(login_url='signin')#dataProduccionInte-list/
@api_view(['GET'])
def ProduccionDataIntegrantePatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id')
    lastEm = int(lastEm[0]['empresa_id'])

    idOperacion = request.GET.get('idOpPatinador', None)
    idIntegrante = request.GET.get('idIntegranteSelectPatinador')
    dontrepeYorself = []
    tareas = []
    patinadores = []
    for tareasIntegrante in Prod.objects.filter(empresa_id=lastEm, operacion_id=int(idOperacion), integrante_id=idIntegrante).distinct().values('tarea_id', 'patinador_id'):
        tareaIntegrante = (Tarea.objects.filter(
            empresa_id=lastEm, id=tareasIntegrante['tarea_id']).values('nom_tarea', 'id')[0])
        totalIntegrante = Prod.objects.filter(empresa_id=lastEm, operacion_id=int(idOperacion), integrante_id=idIntegrante, tarea_id=tareaIntegrante['id']).values(
            'tarea_id', 'can_terminada').aggregate(can_terminada=Sum('can_terminada'))
        patinador = Patinador.objects.filter(
            empresa_id=lastEm, id=tareasIntegrante['patinador_id']).distinct().values('integrante_id')
        patinador = Integrante.objects.filter(
            empresa_id=lastEm, id=patinador[0]['integrante_id']).values('nombres', 'apellidos')
        patinador = "{} {}".format(
            patinador[0]['nombres'], patinador[0]['apellidos'])
        if patinador in patinadores:
            pass
        else:
            patinadores.append(patinador)
        if tareaIntegrante['nom_tarea'] in dontrepeYorself:
            pass
        else:
            dontrepeYorself.append(tareaIntegrante['nom_tarea'])
            tareas.append({
                'tarea': tareaIntegrante['nom_tarea'],
                'cat_total_tarea': totalIntegrante['can_terminada'],
            })
    if tareas == []:
        pass
    else:
        if patinadores == []:
            pass
        else:
            tareas.append({'patinadores': patinadores})
    return Response(tareas)

@login_required(login_url='signin')
@api_view(['GET'])
def TareaListPatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id')
    lastEm = int(lastEm[0]['empresa_id'])

    tarea = Tarea.objects.all().filter(empresa_id=lastEm, estatus='A').order_by('-id')
    serializer = TareaSerializer(tarea, many=True)
    return Response(serializer.data)

@login_required(login_url='signin')
@api_view(['GET'])
def integranteListPatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id')
    lastEm = int(lastEm[0]['empresa_id'])

    integrante = Integrante.objects.all().filter(
        empresa_id=lastEm, estatus='A').order_by('-id')
    try:
        serializer = IntegranteSerializer(integrante, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(str(e), "no tienes patinadores activos")
        return Response("no tienes patinadores activos")

@login_required(login_url='signin')
@api_view(['GET'])
def patinadoresActProdPatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)
    lastEm = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id')
    lastEm = int(lastEm[0]['empresa_id'])
    try:
        patinadores = Patinador.objects.all().filter(usuario=idUser, estatus='A',
                                                     ctrlProduccion=1, empresa_id=int(lastEm))
        serializer = PatinadorSerializer(patinadores, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(str(e), "no tienes patinadores activos")
        return Response("no tienes patinadores activos")

@login_required(login_url='signin')
@api_view(['POST'])
def createProduccionPatinador(request,):
    #Prod = Models Produccion
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    integranteConten = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id', 'usuario_id')
    lastEm = int(integranteConten[0]['empresa_id'])    
    
    idPatinador = Patinador.objects.filter(
        integrante_id=idUser.integrante_id).values('id')
    idPatinador = idPatinador[0]['id']
    canTerminada = int(request.data['cantidadProdPatinador'])
    valor = Tarea.objects.get(id=int(request.data['OccionId_tareaPatinador']))

    try:
        obj = Prod.objects.create(usuario_id=int(integranteConten[0]['usuario_id']),
        patinador_id=idPatinador,integrante_id=int(request.data['OccionId_integrante_prodPatinador']),
            empresa_id=int(lastEm),
            operacion_id=int(request.data['idOperacionPatinador']),
            talla_id=int(request.data['OccionId_tallaPatinador']),
            tarea_id=int(request.data['OccionId_tareaPatinador']),
            can_terminada=canTerminada
        )

        obj = Prod.objects.latest('id')
        btnDel = "<button class='btn btn-block btn-sm btn-outline-danger icofont-ui-remove' type='submit' onclick='deleteProduccionUnico({})'> </button>".format(
            obj.id)
        obj = Prod.objects.all().filter(id=obj.id).update(delProduccion=btnDel)
        
        costeProd = Operacion.objects.get(id=int(request.data['idOperacionPatinador']))
        costeProd.costeProd += (canTerminada*valor.valor)
        costeProd.save()

        
        
        data = {
            'produccion': "Produccion guardado con exito!",
            'estatus': True
        }

        return Response(data)

    except Exception as e:
        print(str(e))
        return Response("PRODUCCION no cargadA " + str(e))


class AcumuladoPatinador(LoginRequiredMixin, TemplateView):
    template_name = "pages/blackbox/acumuladoPerfilPatinador.html"
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(AcumuladoPatinador, self).get_context_data(**kwargs)
        s = SessionStore()
        s['last_login']  = self.request.user.pk
        s.create()
        myuser           = MyUser.objects.get(id=s['last_login'])
        integranteConten = Integrante.objects.filter(id=myuser.integrante_id).values('empresa_id', 'usuario_id')
        lastEm           = int(integranteConten[0]['empresa_id'])
        AllEmpresa       = RelacionEmpresa.objects.filter(usuario_id=int(integranteConten[0]['usuario_id']))
        EmpresaActual    = Empresa.objects.filter(usuario=int(integranteConten[0]['usuario_id']), id=int(lastEm))

        context = super(AcumuladoPatinador, self).get_context_data(**kwargs)
        context['lastIdEmpresa'] = int(lastEm)  # ids empresas
        context['nomEmpresa'] = AllEmpresa  # nombre de todas las empresa
         # nombre de la empresa actual
        context['nomEmpresaU'] = EmpresaActual
        context['last_login'] = s['last_login']    # ultimo inicio de seccion
        
        try:
            patinadores = Patinador.objects.all().filter(usuario=int(
                integranteConten[0]['empresa_id']), empresa_id=int(lastEm)).values('integrante_id')
            allPatinadores = Integrante.objects.all().filter(usuario=int(integranteConten[0]['empresa_id']), empresa_id=int(
                lastEm), id=int(patinadores[0].get('integrante_id'))).values('nombres', 'apellidos', 'id')
            # todos los patinadores de la empresa
            context['allPatinador'] = allPatinadores
            return context
        finally:
            return context

@login_required(login_url='signin')#tabla principal Acumulado Patinador
@api_view(['GET'])
def AcumuladoListPatinadores(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = Integrante.objects.filter(id=idUser.integrante_id).values('empresa_id')
    
    
    lastEm = int(lastEm[0]['empresa_id'])
    acumuladoQsect = ACUMULADO.objects.filter(
        empresa_id=lastEm, estatus='A').order_by('-id')
    AcumuladoSe = AcumuladoSerializer(acumuladoQsect, many=True)
    dump = json.dumps(AcumuladoSe.data)  # dump serializer to json reponse

    return HttpResponse(dump, content_type='application/json')

@login_required(login_url='signin')
@api_view(['GET'])
def AcumuladoDataIntegrantePatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    integranteConten = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id', 'usuario_id')
    lastEm = int(integranteConten[0]['empresa_id'])
    idAcumulado = request.GET.get('idAcumuladoPatinador', None)

    idIntegrante = request.GET.get('idIntegranteSelectPatinador')
    dontrepeYorself = []
    tareas = []
    patinadores = []

    for tareasIntegrante in ProAcu.objects.filter(usuario_id=int(integranteConten[0]['usuario_id']), empresa_id=lastEm, acumulado_id=int(idAcumulado),
                                                  integrante_id=idIntegrante).distinct().values('tarea_id', 'patinador_id'):
        tareaIntegrante = (Tarea.objects.filter(usuario_id=int(
            integranteConten[0]['usuario_id']), empresa_id=lastEm, id=tareasIntegrante['tarea_id']).values('nom_tarea', 'id')[0])
        totalIntegrante = ProAcu.objects.filter(usuario_id=int(integranteConten[0]['usuario_id']), empresa_id=lastEm, acumulado_id=int(
            idAcumulado), integrante_id=idIntegrante, tarea_id=tareaIntegrante['id']).values('tarea_id', 'can_prod_acum').aggregate(can_prod_acum=Sum('can_prod_acum'))
        patinador = Patinador.objects.filter(usuario_id=int(
            integranteConten[0]['usuario_id']), empresa_id=lastEm, id=tareasIntegrante['patinador_id']).distinct().values('integrante_id')
        patinador = Integrante.objects.filter(usuario_id=int(
            integranteConten[0]['usuario_id']), empresa_id=lastEm, id=patinador[0]['integrante_id']).values('nombres', 'apellidos')
        patinador = "{} {}".format(
            patinador[0]['nombres'], patinador[0]['apellidos'])

        if patinador in patinadores:pass
        else:patinadores.append(patinador)
        if tareaIntegrante['nom_tarea'] in dontrepeYorself:pass
        else:
            dontrepeYorself.append(tareaIntegrante['nom_tarea'])
            tareas.append({
                'tarea': tareaIntegrante['nom_tarea'],
                'cat_total_tarea': totalIntegrante['can_prod_acum'],
            })
    if tareas == []:pass
    else:
        if patinadores == []:pass
        else:tareas.append({'patinadores': patinadores})
    return Response(tareas)

@login_required(login_url='signin')
@api_view(['GET'])
def AcumuladoListProcPatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    integranteConten = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id', 'usuario_id')
    lastEm = int(integranteConten[0]['empresa_id'])
    idAcumulado = request.GET.get('idAcumuladoPatinador', None)
    acumuladoProc = ProAcu.objects.filter(usuario_id=int(
        integranteConten[0]['usuario_id']), empresa_id=lastEm, acumulado_id=idAcumulado).order_by('-id')
    serializer = AcuSerializerProc(acumuladoProc, many=True)
    return Response(serializer.data)

@login_required(login_url='signin')
@api_view(['POST'])
def createProAcumuladoPatinador(request,):

    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)
    integranteConten = Integrante.objects.filter(id=idUser.integrante_id).values('empresa_id', 'usuario_id', 'id')
    lastEm = int(integranteConten[0]['empresa_id'])
    canTerminada = int(request.data['Cantidad_AcuPatinador'])
        
    acumulado_id = int(request.data['acumulado_idPatinador'])
    valor = Tarea.objects.get(id=int(request.data['OccionId_tarea_AcuPatinador']))

    idPatinador = Patinador.objects.filter(
        integrante_id=idUser.integrante_id).values('id')
    idPatinador = idPatinador[0]['id']
    
    try:
        obj = ProAcu.objects.create(
            usuario_id=int(integranteConten[0]['usuario_id']),
            empresa_id=int(lastEm),
            integrante_id=int(request.data['OccionId_integrante_AcuPatinador']),
            patinador_id=idPatinador,
            tarea_id=int(request.data['OccionId_tarea_AcuPatinador']),
            talla_id=int(request.data['OccionId_talla_AcuPatinador']),
            can_prod_acum=canTerminada,
            acumulado_id=acumulado_id
        )

        obj = ProAcu.objects.latest('id')
        btnDel = "<button class='btn btn-block btn-sm btn-outline-danger icofont-ui-remove' type='submit' onclick='deleteAcumuladoUnico({})'> </button>".format(
            obj.id)
        obj = ProAcu.objects.all().filter(id=obj.id).update(delAcumulProc=btnDel)

        #suma de la cantidad 
        costeA = ACUMULADO.objects.get(id=acumulado_id)
        costeA.costeAcu += (canTerminada*valor.valor)
        costeA.save()  # "{:10.4f}".format(x)

        data = {
            'Acumulado': "Acumulado guardado con exito!",
            'estatus': True
        }

    except Exception as e:
        data = {'Acumulado': str(e), 'estatus': False}
        return Response(data)

    return Response(data)

@login_required(login_url='signin')
@api_view(['GET'])
def TallaEmpresaListPatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = Integrante.objects.filter(id=idUser.integrante_id).values('empresa_id')
    lastEm = int(lastEm[0]['empresa_id'])
    ptalla = Talla.objects.filter(empresa_id=lastEm).order_by('-id')

    serializer = TallaSerializer(ptalla, many=True)

    return Response(serializer.data)


class CasinoHomePatinador(LoginRequiredMixin, TemplateView):
    template_name = "pages/blackbox/casinoActivoPerfilPatinador.html"
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CasinoHomePatinador, self).get_context_data(**kwargs)
        s = SessionStore()
        s['last_login'] = self.request.user.pk
        s.create()

        integranteConten = Integrante.objects.filter(
            id=s['last_login']).values('empresa_id', 'usuario_id')
        AllEmpresa = RelacionEmpresa.objects.filter(
            usuario_id=(integranteConten[0]['usuario_id']))

        #lastEm=Integrante.objects.filter(id=s['last_login']).values('empresa_id')
        lastEm = int(integranteConten[0]['empresa_id'])

        Tallas = Talla.objects.filter(usuario=int(integranteConten[0]['usuario_id']), empresa_id=int(
            lastEm)).values('id', 'nom_talla', 'num_talla')
        EmpresaActual = Empresa.objects.filter(usuario=int(
            integranteConten[0]['usuario_id']), id=int(lastEm))

        Operaciones = Operacion.objects.filter(usuario=int(integranteConten[0]['usuario_id']), empresa_id=int(
            lastEm), estatus='A').values('nom_operacion', 'id')
        context = super(CasinoHomePatinador, self).get_context_data(**kwargs)
         # aqui se obtiene el user id
        context['login_user_id'] = s['last_login']
        context['lastIdEmpresa'] = int(lastEm)  # ids empresas
        context['allTalla'] = Tallas  # todaslas las tallas
        context['allOperaciones'] = Operaciones  # todaslas operaciones
        context['nomEmpresa'] = AllEmpresa  # nombre de todas las empresa
        # nombre de la empresa actual
        context['nomEmpresaU'] = EmpresaActual
        context['last_login'] = s['last_login']    # ultimo inicio de seccion
        try:
            patinadores = Patinador.objects.all().filter(usuario=int(
                integranteConten[0]['usuario_id']), empresa_id=int(lastEm)).values('integrante_id')
            allPatinadores = Integrante.objects.all().filter(usuario=int(integranteConten[0]['usuario_id']), empresa_id=int(
                lastEm), id=int(patinadores[0].get('integrante_id'))).values('nombres', 'apellidos', 'id')
            # todos los patinadores de la empresa
            context['allPatinador'] = allPatinadores
            return context
        finally:
            return context

@login_required(login_url='signin')
@api_view(['GET'])
def casinoListPatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id')
    lastEm = int(lastEm[0]['empresa_id'])
    casinos = Casino.objects.filter(
        empresa_id=lastEm, estatus='A').order_by('-id')
    serializer = CasinoSerializer(casinos, many=True)
    return Response(serializer.data)

@login_required(login_url='signin')
@api_view(['GET'])
def ProduccionOPListPatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id')
    lastEm = int(lastEm[0]['empresa_id'])

    produccion = Prod.objects.filter(empresa_id=lastEm, operacion_id=int(
        request.GET.get('idOp', None))).order_by('-id')
    ProduccionSe = ProduccionSerializer(produccion, many=True)
    dump = json.dumps(ProduccionSe.data)  # dump serializer to json reponse

    return HttpResponse(dump, content_type='application/json')

@login_required(login_url='signin')
@api_view(['GET'])
def totalImporteIntePatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)
    integranteConten = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id', 'usuario_id')
    lastEm = int(integranteConten[0]['empresa_id'])

    idCasino = request.GET.get('idCasinoPatinador', None)
    idIntegranteSelect = request.GET.get('idIntegranteSelectPatinador', None)
    casinoImporte = Importe.objects.filter(empresa_id=lastEm, usuario_id=int(
        integranteConten[0]['usuario_id']), integrante_id=idIntegranteSelect, casino_id=int(idCasino)).aggregate(cantidad=Sum('cantidad'))
    cedula = Integrante.objects.filter(id=idIntegranteSelect, empresa_id=lastEm, usuario_id=int(
        integranteConten[0]['usuario_id'])).distinct().values('cedula')
    cedula = cedula[0]['cedula']
    TotalCasinoImporte = casinoImporte['cantidad']
    data = {'TotalCasinoImporte': TotalCasinoImporte,
            'cedulaIntegrante': cedula}
    return JsonResponse(data)

@login_required(login_url='signin')
@api_view(['GET'])
def CasinoDataIntegranteImportePatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)
    integranteConten = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id', 'usuario_id')
    lastEm = int(integranteConten[0]['empresa_id'])
    idCasino = request.GET.get('idCasinoPatinador', None)
    idIntegrante = request.GET.get('idIntegranteSelectPatinador')
    importeCasino = Importe.objects.filter(usuario_id=int(integranteConten[0]['usuario_id']), empresa_id=lastEm, casino_id=int(idCasino),
                                           integrante_id=idIntegrante)
    serializer = ImporteSerializer(importeCasino, many=True)
    return Response(serializer.data)

@login_required(login_url='signin')
@api_view(['GET'])
def CasinoDataImportePatinador(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    integranteConten = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id', 'usuario_id')
    lastEm = int(integranteConten[0]['empresa_id'])
    idCasino = request.GET.get('idCasinoPatinador', None)
    importeGeneral = Importe.objects.filter(usuario_id=int(
        integranteConten[0]['usuario_id']), casino_id=idCasino, empresa_id=lastEm).order_by("-id")
    serializer = ImporteSerializer(importeGeneral, many=True)

    return Response(serializer.data)

@login_required(login_url='signin')
@api_view(['POST'])
def createProCasinoPatinador(request,):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    integranteConten = Integrante.objects.filter(
        id=idUser.integrante_id).values('empresa_id', 'usuario_id', 'id')

    lastEm = int(integranteConten[0]['empresa_id'])
    idCasino = request.data['idCasinoP']
    idPatinador = Patinador.objects.filter(
        integrante_id=integranteConten[0]['id']).values('id')
    idPatinador = idPatinador[0]['id']
    canTerminada = int(request.data['Cantidad_CasinoPatinador'])
    try:
        obj = Importe.objects.create(
            usuario_id=int(integranteConten[0]['usuario_id']),
            empresa_id=int(lastEm),
            integrante_id=int(
                request.data['OccionId_integrante_CasinoPatinador']),
            patinador_id=int(idPatinador),
            cantidad=canTerminada,
            casino_id=int(idCasino)
        )
        Casino.objects.all().filter(id=int(idCasino)).update(
            can_total=F('can_total') + canTerminada)
        obj = Importe.objects.latest('id')
        btnDel = "<button class='btn btn-block btn-sm btn-outline-danger icofont-ui-remove' type='submit' onclick='deleteImporteUnico({})'> </button>".format(
            obj.id)
        obj = Importe.objects.all().filter(id=obj.id).update(delCasinoImport=btnDel)

        data = {
            'Acumulado': "Casino guardado con exito!",
            'estatus': True
        }

    except Exception as e:
        print(str(e))
        data = {'Errror': str(e), 'estatus': False}
        return Response(data)

    return Response(data)
