from django.forms import CharField
from rest_framework import serializers
from produccion.models import Produccion
from patinador.models import Patinador


class PatinadorSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    nomPatinador = serializers.CharField(source='patinador.integrante.nombres')
    apellPatinador = serializers.CharField(source='patinador.integrante.apellidos')
    cedulaPatinador = serializers.CharField(
        source='patinador.integrante.cedula')

    class Meta:
        model = Produccion
        fields = '__all__'




class ProdIntegranSeguimiento(serializers.ModelSerializer):

    
    nomIntegrante = serializers.CharField(source='integrante.nombres')
    apeIntegrante = serializers.CharField(source='integrante.apellidos')
    cedulaIntegrante = serializers.CharField(source='integrante.cedula')
    nomTarea = serializers.CharField(source='tarea.nom_tarea')
    valorTarea = serializers.CharField(source='tarea.valor')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    fecha_cierre = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
#    nomTalla=serializers.CharField(source = 'talla.nom_talla')

    class Meta:
        model = Produccion
        fields = '__all__'


