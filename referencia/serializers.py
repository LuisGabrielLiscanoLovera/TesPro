


from rest_framework import serializers
from .models import Referencia

class ReferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referencia
        fields = '__all__' #['empresa','nom_referencia', 'descripcion']

