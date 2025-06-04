from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Acessorio'

router = routers.DefaultRouter()
router.register('', views.AcessorioVeiculoViewSet, basename='Acessorio')

urlpatterns = [
    path('', include(router.urls) )
]