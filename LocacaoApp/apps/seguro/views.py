from django.shortcuts import render
from .models import Seguro
from .serializer import SeguroSerializer
from rest_framework import viewsets

class EnderecoMViewSet(viewsets.ModelViewSet):
    queryset = Seguro.objects.all()
    serializer_class = SeguroSerializer