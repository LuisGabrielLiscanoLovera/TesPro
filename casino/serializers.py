from rest_framework import serializers
from .models import Casino

class CasinoSerializer(serializers.ModelSerializer):
    nomIntegrante    = serializers.CharField(source='integrante.nombres')
    apelIntegrante   = serializers.CharField(source='integrante.apellidos')
    cedulaIntegrante = serializers.CharField(source='integrante.cedula')

#    category_name = serializers.RelatedField(source='category', read_only=True)

  
    class Meta:
        model = Casino
        fields = '__all__' #all fields
