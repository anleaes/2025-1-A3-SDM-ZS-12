from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'carrinholocacao' 

router = routers.DefaultRouter()
router.register('', views.CarrinhoLocacaoViewSet, basename='carrinho_locacao')

urlpatterns = [
    path('', include(router.urls) )
]