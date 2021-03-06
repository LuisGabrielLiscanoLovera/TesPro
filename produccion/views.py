from django.views.generic import View
import json
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.contrib.sessions.backends.db import SessionStore
from rest_framework.response import Response
from empresa.models import Empresa, RelacionEmpresa, CambioEmpres
from talla.models import Talla
from tarea.models import Tarea
from operacion.models import Operacion
from patinador.models import Patinador
from integrante.models import Integrante
from produccion.models import Produccion as Prod
from django.db.models import Sum
from authapp.models import MyUser
from .serializers import ProduccionSerializer
from patinador.serializers import PatinadorSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.mixins import LoginRequiredMixin
from operacion.serializers import OperacionSerializer
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

class Produccion(LoginRequiredMixin, TemplateView):
    template_name = "pages/produccion.html"
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Produccion, self).get_context_data(**kwargs)

        s = SessionStore()
        s['last_login'] = self.request.user.pk
        s.create()
        AllEmpresa = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])
        lastEm = CambioEmpres.objects.filter(usuario_id=s['last_login']).last()
        Tallas = Talla.objects.filter(usuario=s['last_login'], empresa_id=int(
            lastEm.lastEm)).values('id', 'nom_talla', 'num_talla')
        EmpresaActual = Empresa.objects.filter(
            usuario=s['last_login'], id=int(lastEm.lastEm))
        Operaciones = Operacion.objects.filter(usuario=s['last_login'], empresa_id=int(
            lastEm.lastEm), estatus='A').values('nom_operacion', 'id')
        context = super(Produccion, self).get_context_data(**kwargs)
        # aqui se obtiene el user id
        context['login_user_id'] = s['last_login']
        context['lastIdEmpresa'] = int(lastEm.lastEm)  # ids empresas
        context['allTalla'] = Tallas  # todaslas las tallas
        context['allOperaciones'] = Operaciones  # todaslas operaciones
        context['nomEmpresa'] = AllEmpresa  # nombre de todas las empresa
        # nombre de la empresa actual
        context['nomEmpresaU'] = EmpresaActual
        context['last_login'] = s['last_login']    # ultimo inicio de seccion

        try:
            patinadores = Patinador.objects.all().filter(
                usuario=s['last_login'], empresa_id=int(lastEm.lastEm)).values('integrante_id')
            allPatinadores = Integrante.objects.all().filter(usuario=s['last_login'], empresa_id=int(
                lastEm.lastEm), id=int(patinadores[0].get('integrante_id'))).values('nombres', 'apellidos', 'id')
            # todos los patinadores de la empresa
            context['allPatinador'] = allPatinadores
            return context
        finally:
            return context


class ProduccionHistorial(LoginRequiredMixin, TemplateView):
    template_name = "pages/historial/produccionHistorial.html"
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ProduccionHistorial, self).get_context_data(**kwargs)

        s = SessionStore()
        s['last_login'] = self.request.user.pk
        s.create()
        AllEmpresa = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])
        lastEm = CambioEmpres.objects.filter(usuario_id=s['last_login']).last()
        Tallas = Talla.objects.filter(usuario=s['last_login'], empresa_id=int(
            lastEm.lastEm)).values('id', 'nom_talla', 'num_talla')
        EmpresaActual = Empresa.objects.filter(
            usuario=s['last_login'], id=int(lastEm.lastEm))
        Operaciones = Operacion.objects.filter(usuario=s['last_login'], empresa_id=int(
            lastEm.lastEm), estatus='A').values('nom_operacion', 'id')
        context = super(ProduccionHistorial, self).get_context_data(**kwargs)
        # aqui se obtiene el user id
        context['login_user_id'] = s['last_login']
        context['lastIdEmpresa'] = int(lastEm.lastEm)  # ids empresas
        context['allTalla'] = Tallas  # todaslas las tallas
        context['allOperaciones'] = Operaciones  # todaslas operaciones
        context['nomEmpresa'] = AllEmpresa  # nombre de todas las empresa
        # nombre de la empresa actual
        context['nomEmpresaU'] = EmpresaActual
        context['last_login'] = s['last_login']    # ultimo inicio de seccion

        try:
            patinadores = Patinador.objects.all().filter(
                usuario=s['last_login'], empresa_id=int(lastEm.lastEm)).values('integrante_id')
            allPatinadores = Integrante.objects.all().filter(usuario=s['last_login'], empresa_id=int(
                lastEm.lastEm), id=int(patinadores[0].get('integrante_id'))).values('nombres', 'apellidos', 'id')
            # todos los patinadores de la empresa
            context['allPatinador'] = allPatinadores
            return context
        finally:
            return context


class ValorProduccion(LoginRequiredMixin, TemplateView):
    template_name = "pages/contador/produccionValor.html"
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ValorProduccion, self).get_context_data(**kwargs)

        s = SessionStore()
        s['last_login'] = self.request.user.pk
        s.create()
        AllEmpresa = RelacionEmpresa.objects.filter(usuario_id=s['last_login'])
        lastEm = CambioEmpres.objects.filter(usuario_id=s['last_login']).last()
        Tallas = Talla.objects.filter(usuario=s['last_login'], empresa_id=int(
            lastEm.lastEm)).values('id', 'nom_talla', 'num_talla')
        EmpresaActual = Empresa.objects.filter(
            usuario=s['last_login'], id=int(lastEm.lastEm))
        Operaciones = Operacion.objects.filter(usuario=s['last_login'], empresa_id=int(
            lastEm.lastEm), estatus='A').values('nom_operacion', 'id')
        context = super(ValorProduccion, self).get_context_data(**kwargs)
        # aqui se obtiene el user id
        context['login_user_id'] = s['last_login']
        context['lastIdEmpresa'] = int(lastEm.lastEm)  # ids empresas
        context['allTalla'] = Tallas  # todaslas las tallas
        context['allOperaciones'] = Operaciones  # todaslas operaciones
        context['nomEmpresa'] = AllEmpresa  # nombre de todas las empresa
        # nombre de la empresa actual
        context['nomEmpresaU'] = EmpresaActual
        context['last_login'] = s['last_login']    # ultimo inicio de seccion

        try:
            patinadores = Patinador.objects.all().filter(
                usuario=s['last_login'], empresa_id=int(lastEm.lastEm)).values('integrante_id')
            allPatinadores = Integrante.objects.all().filter(usuario=s['last_login'], empresa_id=int(
                lastEm.lastEm), id=int(patinadores[0].get('integrante_id'))).values('nombres', 'apellidos', 'id')
            # todos los patinadores de la empresa
            context['allPatinador'] = allPatinadores
            return context
        finally:
            return context


class deleteAllProduccion(View):
    def get(self, request):
        idOperacion = request.GET.get('idOperacion', None)
        costeA = Operacion.objects.get(id=idOperacion)
        costeA.costeProd *= 0
        costeA.save()
        Prod.objects.filter(operacion_id=idOperacion).delete()
        data = {'deleted': True}
        return JsonResponse(data)


@login_required(login_url='signin')
@api_view(['GET'])
def ProduccionOPList(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
    produccion = Prod.objects.filter(empresa_id=lastEm.lastEm, operacion_id=int(
        request.GET.get('idOp', None))).order_by('-id')
    ProduccionSe = ProduccionSerializer(produccion, many=True)
    dump = json.dumps(ProduccionSe.data)  # dump serializer to json reponse

    return HttpResponse(dump, content_type='application/json')


@login_required(login_url='signin')
# dataProduccionInte-list/
@api_view(['GET'])
def ProduccionDataIntegrante(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)
    lastEm = CambioEmpres.objects.filter(usuario_id=idUser).last()
    idOperacion = request.GET.get('idOp', None)
    idIntegrante = request.GET.get('idIntegranteSelect')
    dontrepeYorself = []
    tareas = []
    patinadores = []
    for tareasIntegrante in Prod.objects.filter(empresa_id=lastEm.lastEm, operacion_id=int(idOperacion), integrante_id=idIntegrante).distinct().values('tarea_id', 'patinador_id'):
        tareaIntegrante = (Tarea.objects.filter(
            empresa_id=lastEm.lastEm, id=tareasIntegrante['tarea_id']).values('nom_tarea', 'id')[0])
        totalIntegrante = Prod.objects.filter(empresa_id=lastEm.lastEm, operacion_id=int(
            idOperacion), integrante_id=idIntegrante, tarea_id=tareaIntegrante['id']).values('tarea_id', 'can_terminada').aggregate(can_terminada=Sum('can_terminada'))
        patinador = Patinador.objects.filter(
            empresa_id=lastEm.lastEm, id=tareasIntegrante['patinador_id']).distinct().values('integrante_id')
        patinador = Integrante.objects.filter(
            empresa_id=lastEm.lastEm, id=patinador[0]['integrante_id']).values('nombres', 'apellidos')
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
def ProduccionDataIntegranteValor(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)
    lastEm = CambioEmpres.objects.filter(usuario_id=idUser).last()
    idOperacion = request.GET.get('idOp', None)
    idIntegrante = request.GET.get('idIntegranteSelect')
    totalGenerado = 0
    dontrepeYorself = []
    tareas = []
    patinadores = []
    for tareasIntegrante in Prod.objects.filter(empresa_id=lastEm.lastEm, operacion_id=int(idOperacion), integrante_id=idIntegrante).distinct().values('tarea_id', 'patinador_id'):
        tareaIntegrante = (Tarea.objects.filter(empresa_id=lastEm.lastEm,
                           id=tareasIntegrante['tarea_id']).values('nom_tarea', 'id', 'valor')[0])
        totalIntegrante = Prod.objects.filter(empresa_id=lastEm.lastEm, operacion_id=int(
            idOperacion), integrante_id=idIntegrante, tarea_id=tareaIntegrante['id']).values('tarea_id', 'can_terminada').aggregate(can_terminada=Sum('can_terminada'))
        patinador = Patinador.objects.filter(
            empresa_id=lastEm.lastEm, id=tareasIntegrante['patinador_id']).distinct().values('integrante_id')
        patinador = Integrante.objects.filter(
            empresa_id=lastEm.lastEm, id=patinador[0]['integrante_id']).values('nombres', 'apellidos')
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
            ValorTotalTarea = int(
                int(tareaIntegrante['valor']))*(int(totalIntegrante['can_terminada']))
            totalGenerado += ValorTotalTarea
            tareas.append({
                'tarea': tareaIntegrante['nom_tarea'],
                'cat_total_tarea': totalIntegrante['can_terminada'],
                'valorTarea': "$ {:0,.2f}".format(tareaIntegrante['valor']),
                'ValorTotalTarea': "$ {:0,.2f}".format(ValorTotalTarea),
            })
    if tareas == []:
        pass
    else:
        if patinadores == []:
            pass
        else:
            tareas.append({'patinadores': patinadores,
                          'totalGenerado': "$ {:0,.2f}".format(totalGenerado)})

    return Response(tareas)


@login_required(login_url='signin')
@api_view(['GET'])  
def operacionesListValor(request):     
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)

    lastEm     = CambioEmpres.objects.filter(usuario_id=idUser).last()   
    despacho = Operacion.objects.filter(
        empresa_id=lastEm.lastEm).order_by('-created_at')
    serializer = OperacionSerializer(despacho, many=True)
    
    return Response(serializer.data)


@login_required(login_url='signin')
@api_view(['POST'])
def createProduccion(request,):
    # Prod = Models Produccion
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
    canTerminada = int(request.data['cantidadProd'])
    valor = Tarea.objects.get(id=int(request.data['OccionId_tarea']))

    try:
        obj = Prod.objects.create(
            usuario_id=int(idUser.id),
            patinador_id=int(request.data['OccionId_pantinador_prod']),
            integrante_id=int(request.data['OccionId_integrante_prod']),
            empresa_id=int(lastEm.lastEm),
            operacion_id=int(request.data['idOperacion']),
            talla_id=int(request.data['OccionId_talla']),
            tarea_id=int(request.data['OccionId_tarea']),
            can_terminada=canTerminada
        )

        obj = Prod.objects.latest('id')
        btnDel = "<button class='btn btn-block btn-sm btn-outline-danger icofont-ui-remove' type='submit' onclick='deleteProduccionUnico({})'> </button>".format(
            obj.id)
        obj = Prod.objects.all().filter(id=obj.id).update(delProduccion=btnDel)

        costeProd = Operacion.objects.get(id=int(request.data['idOperacion']))
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


@login_required(login_url='signin')
@api_view(['DELETE'])
def deleteProduccion(request, id):
    try:
        ProOp = Prod.objects.all().filter(id=id).values(
            'can_terminada', 'operacion_id', 'tarea_id')
        valor = Tarea.objects.get(id=int(ProOp[0]['tarea_id']))
        costeA = Operacion.objects.get(id=ProOp[0]['operacion_id'])
        costeA.costeProd -= (int(ProOp[0]['can_terminada'])*valor.valor)
        costeA.save()  # "{:10.4f}".format(x)
        Prod.objects.get(id=id).delete()
        data = {
            'deleted': True
        }

    except Exception as e:
        print(str(e))

        data = {
            'deleted': False
        }

        Response("Unable to Delete Task!")
    return JsonResponse(data)


@login_required(login_url='signin')
@api_view(['GET'])
def patinadoresActProd(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)
    lastEm = CambioEmpres.objects.filter(usuario_id=idUser).last()
    lastEm = lastEm.lastEm
    try:
        patinadores = Patinador.objects.all().filter(usuario=idUser, estatus='A',
                                                     ctrlProduccion=1, empresa_id=int(lastEm))
        serializer = PatinadorSerializer(patinadores, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(str(e), "no tienes patinadores activos")
        return Response("no tienes patinadores activos")
