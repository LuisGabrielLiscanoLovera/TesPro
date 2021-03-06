from django.shortcuts import redirect
from colorDev.models import Color
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils import (dateformat, formats)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ColorSerializer
from empresa.models import CambioEmpres
from authapp.models import MyUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/color-list/'
		}
	return Response(api_urls)
@login_required(login_url='signin')
@api_view(['GET'])
def colorList(request):
    if request.session.has_key('username'):        
        if 'username' in request.session:
            username = request.session['username']     
            idUser   = MyUser.objects.get(username=username)
            
    
    lastEm     = CambioEmpres.objects.filter(usuario_id=idUser).last()
    lastEm=lastEm.lastEm
    colores = Color.objects.all().filter(empresa_id=lastEm).order_by('-id')    
    serializer = ColorSerializer(colores, many=True)
    serializer.data
    return Response(serializer.data)






class CreateColor(View):
    def  get(self, request):
        
        if request.session.has_key('username'):        
            if 'username' in request.session:
                username = request.session['username']     
                idUser   = MyUser.objects.get(username=username)
        
        
        lastEm           = CambioEmpres.objects.filter(usuario_id=idUser.id).last()
        nom_color = request.GET.get('nom_color', None)
        codigo_color    = request.GET.get('codigo_color', None)
        existeColor   =  Color.objects.extra(where=["nom_color='%s' AND usuario_id = '%s' AND empresa_id = '%s'" %(nom_color,idUser.id,lastEm.lastEm) ])
        if existeColor.count()==0:    
       # agregar empresa y usuario
            obj = Color.objects.create(
            nom_color      = nom_color,
            codigo_color   = codigo_color,
            empresa_id     = lastEm.lastEm,
            usuario_id     = idUser.id,            
        )
            obj = Color.objects.latest('id')
            user = {'id':obj.id,'nom_color':obj.nom_color,'codigo_color':obj.codigo_color,'created_at':obj.created_at.strftime("%Y-%m-%d %H:%M:%S")}
            data = {
            'user': user
        }
        else:
            data = {
            'user': "enviar un mensaje de error color repetido"
        }     
        return JsonResponse(data)



class DeleteColor(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Color.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)




class UpdateColor(LoginRequiredMixin,TemplateView):
    def  get(self, request):        
        idColor    = request.GET.get('idColor', None)
        nom_color = request.GET.get('nom_color', None)
        codigo_color    = request.GET.get('codigo_color', None)
        idEmpresa       = request.GET.get('empresaUP', None)
        idUser          = request.GET.get('idUserUP', None)
              
        obj = Color.objects.get(id=idColor)
        obj.nom_color = nom_color
        obj.codigo_color = codigo_color
        obj.empresa_id = idEmpresa
        obj.usuario_id = idUser
        try:
            obj.save()
            return redirect('home')
        except Exception as e:  print("reparar peo de cors header crsf token")






