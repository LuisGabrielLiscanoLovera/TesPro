from rest_framework import serializers
from .models import Operacion
from talla.models import Talla
class OperacionSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    fecha_cierre = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    nomReferencia=serializers.CharField(source = 'referencia.nom_referencia')
    nomColor=serializers.CharField(source = 'color.nom_color')
    codColor=serializers.CharField(source = 'color.codigo_color')
    class Meta:
        model = Operacion
        fields = '__all__'


class TallaSerializerOperacion(serializers.ModelSerializer):
    
    class Meta:
        model = Talla
        fields = ['id','empresa_id']
