from rest_framework import serializers
from .models import Referencia

class ReferenciaSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Referencia
        fields = '__all__' #['empresa','nom_referencia', 'descripcion']

