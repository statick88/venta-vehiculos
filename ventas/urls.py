from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
    path('ventas/', views.listar_ventas, name='listar_ventas'),
]
