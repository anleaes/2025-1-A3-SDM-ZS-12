from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pagamento' 

router = routers.DefaultRouter()
router.register('', views.PagamentoViewSet, basename='pagamento')

urlpatterns = [
    path('', include(router.urls) )
]