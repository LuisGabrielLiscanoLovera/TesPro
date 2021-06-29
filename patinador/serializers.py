from rest_framework import serializers
from .models import Patinador

class PatinadorSerializer(serializers.ModelSerializer):
    nomPatinador   = serializers.CharField(source='integrante.nombres')
    apellPatinador = serializers.CharField(source='integrante.apellidos')
#    category_name = serializers.RelatedField(source='category', read_only=True)

    class Meta:
        model = Patinador
        fields = '__all__'

