from .models import Locacao
from rest_framework import serializers

class LocacaoSerializer(serializers.ModelSerializer):
    nome_cliente = serializers.CharField(source='cliente.nome', read_only=True)
    nome_veiculo = serializers.CharField(source='veiculo.modelo', read_only=True)
    nome_funcionario = serializers.CharField(source='funcionario.nome', read_only=True)

    class Meta:
        model = Locacao
        fields = '__all__'