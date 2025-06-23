from .models import Veiculo
from rest_framework import serializers

class VeiculoSerializer(serializers.ModelSerializer):
    nome_categoria = serializers.CharField(source='categoria.nome', read_only=True)
    nomes_acessorios = serializers.SerializerMethodField()

    class Meta:
        model = Veiculo
        fields = '__all__'

    def get_nomes_acessorios(self, obj):
        return [a.nome for a in obj.acessorios.all()]