from django.db import models

class CategoriaVeiculo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    tipo_combustivel = models.CharField(max_length=20, choices=[
        ("Gasolina", "Gasolina"),
        ("Etanol", "Etanol"),
        ("Flex", "Flex"),
        ("Diesel", "Diesel"),
        ("Elétrico", "Elétrico"),
        ("Hibrido", "Hibrido"),
    ])

    class Meta:
        verbose_name = "Categoria de Veículo"
        verbose_name_plural = "Categorias de Veículos"
        ordering = ['nome']

    def __str__(self):
        return self.nome