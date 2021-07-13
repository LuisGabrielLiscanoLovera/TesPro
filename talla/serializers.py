from rest_framework import serializers
from .models import Talla,CanTalla


class TallaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Talla
        fields = '__all__'

class CanTallaSerializer(serializers.ModelSerializer):
#    nomTalla=serializers.CharField(source = 'talla.nom_talla')

    class Meta:
        model = CanTalla
        fields = '__all__'

