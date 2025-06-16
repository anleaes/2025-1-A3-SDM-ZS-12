from django.db import models
from veiculo.models import Veiculo
from acessorio.models import Acessorio
from cliente.models import Cliente


class CarrinhoLocacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, null=True, blank=True)
    acessorio = models.ForeignKey(Acessorio, on_delete=models.CASCADE, null=True, blank=True)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('carrinho', 'veiculo', 'acessorio')

    def __str__(self):
        item_nome = self.veiculo.modelo if self.veiculo else self.acessorio.nome
        return f"{self.quantidade}x {item_nome}"