from rest_framework import serializers
from .models import Cliente, Vehículo, Venta

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class VehículoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehículo
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'
