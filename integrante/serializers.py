from rest_framework import serializers
from .models import Integrante


class IntegranteSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    nomempresa   = serializers.CharField(source='empresa.nom_empresa')


    class Meta:
        model = Integrante
        fields = '__all__'




