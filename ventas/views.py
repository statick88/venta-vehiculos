from django.shortcuts import render
from .models import Cliente, Vehículo, Venta

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def listar_vehiculos(request):
    vehiculos = Vehículo.objects.all()
    return render(request, 'vehiculos.html', {'vehiculos': vehiculos})

def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas.html', {'ventas': ventas})
