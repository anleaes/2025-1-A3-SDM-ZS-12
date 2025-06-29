"""
URL configuration for LocacaoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('seguro/', include('seguro.urls', namespace='seguro')),
    path('CategoriaVeiculo/', include('CategoriaVeiculo.urls', namespace='CategoriaVeiculo')),
    path('cliente/', include('cliente.urls', namespace='cliente')),
    path('veiculo/', include('veiculo.urls', namespace='veiculo')),
    path('locacao/', include('locacao.urls', namespace='locacao') ),
    path('funcionario/', include('funcionario.urls', namespace='funcionario') ),
    path('pagamento/', include('pagamento.urls', namespace='pagamento') ),
    path('Acessorio/', include('acessorio.urls', namespace='Acessorio') ),
    path('carrinholocacao/', include('carrinholocacao.urls', namespace='carrinholocacao') ),
]
