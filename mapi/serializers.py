from rest_framework import serializers

from .models import Compradores

class CompradoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compradores
        fields = ('id', 'nombre')