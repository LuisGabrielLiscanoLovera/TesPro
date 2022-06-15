
from rest_framework import serializers
from produccion.models import Produccion
from integrante.models import Integrante


class ProduccionSerializer(serializers.ModelSerializer):
    
    nom_talla        = serializers.CharField(source='talla.nom_talla')
    num_talla        = serializers.CharField(source='talla.num_talla')
    nomIntegrante    = serializers.CharField(source='integrante.nombres')
    apeIntegrante    = serializers.CharField(source='integrante.apellidos')
    cedulaIntegrante = serializers.CharField(source='integrante.cedula')
    nomTarea         = serializers.CharField(source='tarea.nom_tarea')
    valorTarea       = serializers.CharField(source='tarea.valor')
    
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    fecha_cierre = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")    
#    nomTalla=serializers.CharField(source = 'talla.nom_talla')

    class Meta:
        model = Produccion
        fields = '__all__'
