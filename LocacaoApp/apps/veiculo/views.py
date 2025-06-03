from django.shortcuts import render
from .models import Veiculo
from .serializer import VeiculoSerializer
from rest_framework import viewsets

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer