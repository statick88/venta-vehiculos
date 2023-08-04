from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', views.ClienteRetrieveUpdateDestroyView.as_view(), name='cliente-retrieve-update-destroy'),
    path('vehiculos/', views.VehículoListCreateView.as_view(), name='vehiculo-list-create'),
    path('vehiculos/<int:pk>/', views.VehículoRetrieveUpdateDestroyView.as_view(), name='vehiculo-retrieve-update-destroy'),
    path('ventas/', views.VentaListCreateView.as_view(), name='venta-list-create'),
    path('ventas/<int:pk>/', views.VentaRetrieveUpdateDestroyView.as_view(), name='venta-retrieve-update-destroy'),
]
