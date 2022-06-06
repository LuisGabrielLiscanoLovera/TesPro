from django.forms import CharField
from rest_framework import serializers
from produccion.models import Produccion
from talla.models import Talla
from tarea.models import Tarea
from integrante.models import Integrante


class ProduccionSerializer(serializers.ModelSerializer):

    
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
