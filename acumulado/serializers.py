
from rest_framework import serializers
from acumulado.models import Acumulado
from acumulado.models import ProAcumulado


class AcumuladoSerializer(serializers.ModelSerializer):   
    
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Acumulado
        fields = '__all__'





class AcuSerializerProc(serializers.ModelSerializer):
    
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")    
    nom_talla        = serializers.CharField(source='talla.nom_talla')
    num_talla        = serializers.CharField(source='talla.num_talla')
    nomIntegrante    = serializers.CharField(source='integrante.nombres')
    apeIntegrante    = serializers.CharField(source='integrante.apellidos')
    cedulaIntegrante = serializers.CharField(source='integrante.cedula')
    nomTarea         = serializers.CharField(source='tarea.nom_tarea')
    valorTarea       = serializers.CharField(source='tarea.valor')
    class Meta:
        model = ProAcumulado
        fields = '__all__'
