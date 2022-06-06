from rest_framework import serializers
from .models import Patinador

class PatinadorSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    nomPatinador   = serializers.CharField(source='integrante.nombres')
    apellPatinador = serializers.CharField(source='integrante.apellidos')
    class Meta:
        model = Patinador
        fields = '__all__'

