
import datetime
import json
from django.shortcuts import redirect
from operacion.models import Operacion
from authapp.models import MyUser
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils import (dateformat, formats)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from operacion.serializers import OperacionSerializer, TallaSerializerOperacion
from empresa.models import CambioEmpres
from talla.models import Talla
from produccion.models import Produccion as Prod
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from referencia.models import Referencia


@login_required(login_url='signin')
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
            'List': '/operacion-list/'

        }
	return Response(api_urls)


#muestra lista de
@login_required(login_url='signin')
@api_view(['GET'])
def operacionList(request):
    #capturamos el inicio de session
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = CambioEmpres.objects.filter(usuario_id=idUser).last()
    operacion = Operacion.objects.filter(
    	usuario_id=idUser, empresa_id=lastEm.lastEm).order_by('-id')
    serializer = OperacionSerializer(operacion, many=True)
    return Response(serializer.data)


class CreateOperacion(View):

    def get(self, request):
        if request.session.has_key('username'):
            if 'username' in request.session:
                username = request.session['username']
                idUser = MyUser.objects.get(username=username)

        lastEm = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
        can_totalOP = request.GET.get('can_totalOP', None)
        idReferenciaOP = request.GET.get('idReferencia', None)
        #idColorOP = request.GET.get('idColorOP', None)
        nomOperacion = request.GET.get('nomOperacion', None).upper()

       # print(lastEm,can_totalOP,idReferenciaOP,idColorOP,nomOperacion+'passsssssssssss')

        #puede existir pero no repetido en la misma empresa
        existOperacion = Operacion.objects.extra(
            #where=["nom_operacion='%s' AND usuario_id = '%s' AND empresa_id = '%s'" % ("OP-"+nomOperacion, idUser.id, lastEm.lastEm)])
            where=["nom_operacion='%s' AND usuario_id = '%s' AND empresa_id = '%s'" % (nomOperacion, idUser.id, lastEm.lastEm)])

        if existOperacion.count() == 0:

            obj = Operacion.objects.create(
                empresa_id=lastEm.lastEm,
                usuario_id=idUser.id,
                #nom_operacion="OP-"+nomOperacion,
                nom_operacion=nomOperacion,
                estatus='A',
               # color_id=int(idColorOP),
                referencia_id=idReferenciaOP,
                can_total=can_totalOP,
                can_restante=can_totalOP
            )

            #aqui me tiene que devolver el las id para trabajar con las tallas
            obj = Operacion.objects.latest('id')
            idEmpresaOP = Operacion.objects.filter(
            	id=obj.id).values('empresa_id')
            tallas = Talla.objects.filter(
            	empresa_id=idEmpresaOP[0]['empresa_id']).order_by('-id')
            serializer = TallaSerializerOperacion(tallas, many=True)

            datas = json.dumps(serializer.data)
            data = {
                'user': "Operacion creaada con exito!",
                'lastIdOperacion': obj.id,
                'tallasEmpresa': datas,
                'estatus': True
            }
        else:
            data = {
                'user': "enviar un mensaje de error operacion repetida",
                'estatus': False
            }
            print("enviar un mensaje de error operacion repetida")

        return JsonResponse(data)


class DeleteOperacion(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Operacion.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateOperacion(LoginRequiredMixin, TemplateView):
    def get(self, request):
        idIpoperacion = request.GET.get('idIpoperacionUP', None)
        idEmpresa = request.GET.get('idEmpresaUP', None)
        idUser = request.GET.get('idUserUP', None)
        nombres = request.GET.get('nombresInputUP', None)
        apellido = request.GET.get('apellidosUP', None)
        sexo = request.GET.get('sexoUP', None)
        estatus = request.GET.get('estatusUP', None)
        correo = request.GET.get('correoUP', None)
        cedula = request.GET.get('cedulaUP', None)
        num_telf = request.GET.get('num_telefonoUP', None)
        direccion = request.GET.get('direccionUP', None)
        abilidad = request.GET.get('abilidadUP', None)

        obj = Operacion.objects.get(id=idIpoperacion)
        obj.empresa_id = idEmpresa
        obj.usuario_id = idUser
        obj.nombres = nombres
        obj.apellido = apellido
        obj.sexo = sexo
        obj.estatus = estatus
        obj.correo = correo
        obj.cedula = cedula
        obj.num_telf = num_telf
        obj.direccion = direccion
        obj.abilidad = abilidad

        try:
            obj.save()
            return redirect('home')
        except Exception as e:
       	    print("reparar peo de cors header crsf token")


@login_required(login_url='signin')
@api_view(['GET'])
def cerrarOP(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = CambioEmpres.objects.filter(usuario_id=idUser.id).last()

    try:
        idOP = int(request.GET['idOP'])
        Operacion.objects.filter(id=idOP, empresa_id=lastEm.lastEm).update(
            estatus="I", fecha_cierre=(Operacion.objects.filter(id=idOP).values('updated_at')))
        Prod.objects.filter(operacion_id=idOP, empresa_id=lastEm.lastEm).update(
            estatus="I", fecha_cierre=(Operacion.objects.filter(id=idOP).values('updated_at')))
        data = {"casino": True, "msj": "operacion cerrardo"}
        return Response(data)
    except Exception as e:
        data = {"casino": False,
                "msj": "operacion No cerrardo", "error": str(e)}
        return Response(data)


@login_required(login_url='signin')
@api_view(['GET'])
def abrirOP(request):
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = CambioEmpres.objects.filter(usuario_id=idUser.id).last()

    try:
        idOP = int(request.GET['idOP'])
        Operacion.objects.filter(id=idOP, empresa_id=lastEm.lastEm).update(
            estatus="A", fecha_cierre=(Operacion.objects.filter(id=idOP).values('updated_at')))
        Prod.objects.filter(operacion_id=idOP, empresa_id=lastEm.lastEm).update(
            estatus="A", fecha_cierre=(Operacion.objects.filter(id=idOP).values('updated_at')))
        data = {"casino": True, "msj": "operacion abierta"}
        return Response(data)
    except Exception as e:
        data = {"casino": False,
                "msj": "operacion No abierta", "error": str(e)}
        return Response(data)

#referencia activas en el formulario


@login_required(login_url='signin')
@api_view(['GET'])
def referenciaList(request):
    #capturamos el inicio de session
    if request.session.has_key('username'):
        if 'username' in request.session:
            username = request.session['username']
            idUser = MyUser.objects.get(username=username)

    lastEm = CambioEmpres.objects.filter(usuario_id=idUser.id).last()

    referencias = []

    for refer in Referencia.objects.filter(empresa_id=lastEm.lastEm, estatus='A').distinct().values('nom_referencia', 'id'):
        referencias.append({
            'nom_referencia_act': refer['nom_referencia'],
            'id': refer['id']
        })

    return Response(referencias) 

