from rest_framework import serializers
from .models import Patinador

class PatinadorSerializer(serializers.ModelSerializer):
    datosPatinador = serializers.CharField(source='nom_patinador.nombres')
#    category_name = serializers.RelatedField(source='category', read_only=True)

    class Meta:
        model = Patinador
        fields = '__all__'

