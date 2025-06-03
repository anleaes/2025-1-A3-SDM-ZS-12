from django.shortcuts import render
from .models import Locacao
from .serializer import LocacaoSerializer
from rest_framework import viewsets

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Locacao.objects.all()
    serializer_class = LocacaoSerializer