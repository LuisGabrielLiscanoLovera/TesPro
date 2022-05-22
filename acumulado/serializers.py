
from rest_framework import serializers
from acumulado.models import Acumulado



class AcumuladoSerializer(serializers.ModelSerializer):   
    
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Acumulado
        fields = '__all__'
