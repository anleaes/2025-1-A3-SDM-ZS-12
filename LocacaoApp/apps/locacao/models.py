from django.db import models
from cliente.models import Cliente
from veiculo.models import Veiculo
from seguro.models import Seguro
from funcionario.models import Funcionario

class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    seguro = models.ForeignKey(Seguro, on_delete=models.SET_NULL, null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_hora_retirada = models.DateTimeField()
    data_hora_prevista_devolucao = models.DateTimeField()
    data_hora_efetiva_devolucao = models.DateTimeField(null=True, blank=True)
    
    valor_total_previsto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ("Agendada", "Agendada"),
        ("Em andamento", "Em andamento"),
        ("Concluída", "Concluída"),
        ("Cancelada", "Cancelada"),
    ])

    def calcular_valor_total(self):
        if self.data_hora_retirada and self.data_hora_prevista_devolucao:
            dias = (self.data_hora_prevista_devolucao - self.data_hora_retirada).days or 1
            valor_diaria = self.veiculo.valor_diaria
            adicional = self.veiculo.categoria.preco_adicional_diaria if self.veiculo.categoria else 0
            return (valor_diaria + adicional) * dias
        return 0

    def save(self, *args, **kwargs):
        self.valor_total_previsto = self.calcular_valor_total()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Locação"
        verbose_name_plural = "Locações"
        ordering = ['-data_hora_retirada']

    def __str__(self):
        return f"Locação #{self.id} - {self.cliente.nome} ({self.status})"