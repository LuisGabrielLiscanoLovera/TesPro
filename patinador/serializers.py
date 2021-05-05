from rest_framework import serializers
from .models import Patinador

class PatinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patinador
        fields = '__all__'

