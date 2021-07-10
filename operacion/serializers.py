from rest_framework import serializers
from .models import Operacion,Talla,CanTalla
class OperacionSerializer(serializers.ModelSerializer):
    nomReferencia=serializers.CharField(source = 'referencia.nom_referencia')
    nomColor=serializers.CharField(source = 'color.nom_color')
    class Meta:
        model = Operacion
        fields = '__all__'

class TallaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Talla
        fields = '__all__'

class CanTallaSerializer(serializers.ModelSerializer):
    nomTalla=serializers.CharField(source = 'talla.nom_talla')

    class Meta:
        model = CanTalla
        fields = '__all__'

