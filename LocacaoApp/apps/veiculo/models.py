from django.db import models
from CategoriaVeiculo.models import CategoriaVeiculo

class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    cor = models.CharField(max_length=30)
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(CategoriaVeiculo, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        ordering = ['placa'] 

    def __str__(self):
        return f"{self.modelo} - {self.placa}"