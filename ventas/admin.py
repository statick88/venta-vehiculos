from django.contrib import admin
from .models import Cliente, Vehiculo, Venta

admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Venta)
