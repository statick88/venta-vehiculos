from rest_framework import generics
from .models import Cliente, Vehículo, Venta
from .serializers import ClienteSerializer, VehículoSerializer, VentaSerializer

class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VehículoListCreateView(generics.ListCreateAPIView):
    queryset = Vehículo.objects.all()
    serializer_class = VehículoSerializer

class VehículoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehículo.objects.all()
    serializer_class = VehículoSerializer

class VentaListCreateView(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
