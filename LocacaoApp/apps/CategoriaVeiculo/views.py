from django.shortcuts import render
from .models import CategoriaVeiculo
from .serializer import CategoriaVeiculoSerializer
from rest_framework import viewsets

class CategoriaVeiculoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaVeiculo.objects.all()
    serializer_class = CategoriaVeiculoSerializer