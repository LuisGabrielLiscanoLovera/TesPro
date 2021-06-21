from rest_framework import serializers
from .models import Patinador

class PatinadorSerializer(serializers.ModelSerializer):
    nomPatinador   = serializers.CharField(source='nom_patinador.nombres')
    apellPatinador = serializers.CharField(source='nom_patinador.apellidos')
#    category_name = serializers.RelatedField(source='category', read_only=True)

    class Meta:
        model = Patinador
        fields = '__all__'

