from django.urls import include, path
from . import views
from rest_framework import routers

app_name = 'seguro'

router = routers.DefaultRouter()
router.register('', views.SeguroViewSet, basename='seguro')

urlpatterns = [
    path('', include(router.urls) )
]