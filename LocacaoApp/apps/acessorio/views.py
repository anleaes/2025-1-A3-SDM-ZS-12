from django.shortcuts import render
from .models import Acessorio
from .serializer import AcessorioSerializer
from rest_framework import viewsets

class AcessorioViewSet(viewsets.ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer