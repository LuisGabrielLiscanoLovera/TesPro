from rest_framework import serializers
from .models import Talla,CanTalla


class TallaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Talla
        fields = '__all__'

class CanTallaSerializer(serializers.ModelSerializer):
    nom_talla=serializers.CharField(source = 'talla.nom_talla')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

#    nomTalla=serializers.CharField(source = 'talla.nom_talla')

    class Meta:
        model = CanTalla
        fields = '__all__'

