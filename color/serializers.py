from rest_framework import serializers
from .models import Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__' #all fields


from .models import  Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        # id is auto generated primary key
        
        fields = ('id', 'item','itemd')