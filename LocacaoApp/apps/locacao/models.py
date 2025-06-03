from django.db import models
from cliente.models import Cliente
from veiculo.models import Veiculo
from seguro.models import Seguro

class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    seguro = models.ForeignKey(Seguro, on_delete=models.SET_NULL, null=True, blank=True)
    
    data_hora_retirada = models.DateTimeField()
    data_hora_prevista_devolucao = models.DateTimeField()
    data_hora_efetiva_devolucao = models.DateTimeField(null=True, blank=True)
    
    valor_total_previsto = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ("Agendada", "Agendada"),
        ("Em andamento", "Em andamento"),
        ("Concluída", "Concluída"),
        ("Cancelada", "Cancelada"),
    ])

    class Meta:
        verbose_name = "Locação"
        verbose_name_plural = "Locações"
        ordering = ['-data_hora_retirada']

    def __str__(self):
        return f"Locação #{self.id} - {self.cliente.nome} ({self.status})"