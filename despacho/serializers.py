from rest_framework import serializers
from .models import Operacion
from .models import Despacho

class OperacionSerializer(serializers.ModelSerializer):
    created_at    = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at    = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    nomReferencia = serializers.CharField(source = 'referencia.nom_referencia')
    nomColor      = serializers.CharField(source = 'color.nom_color')
    codColor      = serializers.CharField(source = 'color.codigo_color')
    class Meta:
        model  = Operacion
        fields = '__all__'



class DespachoSerializer(serializers.ModelSerializer):
    nom_patinador   = serializers.CharField(source='patinador.integrante.nombres')
    apell_patinador = serializers.CharField(source='patinador.integrante.apellidos')
    nom_talla   = serializers.CharField(source='talla.nom_talla')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    id = serializers.IntegerField()
   
    class Meta:
        model = Despacho
        fields = '__all__'
