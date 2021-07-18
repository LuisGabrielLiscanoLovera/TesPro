from rest_framework import serializers
from .models import Casino, Importe

class CasinoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    nomIntegrante    = serializers.CharField(source='integrante.nombres')
    apelIntegrante   = serializers.CharField(source='integrante.apellidos')
    cedulaIntegrante = serializers.CharField(source='integrante.cedula')
    

#    category_name = serializers.RelatedField(source='category', read_only=True)
  
    class Meta:
        model = Casino
        fields = '__all__' #all fields


class ImporteSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")


#    category_name = serializers.RelatedField(source='category', read_only=True)
  
    class Meta:
        model = Importe
        fields = '__all__' #all fields