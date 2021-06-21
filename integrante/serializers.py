from rest_framework import serializers
from .models import Integrante

class IntegranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrante
        fields = '__all__'




