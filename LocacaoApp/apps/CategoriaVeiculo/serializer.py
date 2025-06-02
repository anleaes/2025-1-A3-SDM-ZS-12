from .models import CategoriaVeiculo
from rest_framework import serializers

class CategoriaVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaVeiculo
        fields = '__all__'