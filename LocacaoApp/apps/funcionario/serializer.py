from .models import Funcionario
from rest_framework import serializers

class LocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'