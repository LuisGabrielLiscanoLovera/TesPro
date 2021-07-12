from rest_framework import serializers
from .models import Operacion
class OperacionSerializer(serializers.ModelSerializer):
    nomReferencia=serializers.CharField(source = 'referencia.nom_referencia')
    nomColor=serializers.CharField(source = 'color.nom_color')
    codColor=serializers.CharField(source = 'color.codigo_color')
    class Meta:
        model = Operacion
        fields = '__all__'
