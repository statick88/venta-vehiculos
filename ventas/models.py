from django.db import models

class Cliente(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
class Vehiculo(models.Model):
    
        marca = models.CharField(max_length=50)
        modelo = models.CharField(max_length=50)
        color = models.CharField(max_length=50)
        anio = models.IntegerField()
        precio = models.FloatField()
        tipo = models.CharField(max_length=50)
        foto = models.ImageField(upload_to='vehiculos', null=True)

    
        def __str__(self):
            return self.marca + ' ' + self.modelo

class Venta(models.Model):
        
            cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
            vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
            fecha = models.DateField(auto_now=True)
            costo = models.FloatField(verbose_name='Costo del vehiculo')
            observaciones = models.CharField(max_length=50)
            iva = models.FloatField()
            descuento = models.FloatField()
            total = models.FloatField()
    
            def __str__(self):
                return self.cliente.nombre + ' ' + self.cliente.apellido + ' ' + self.vehiculo.marca + ' ' + self.vehiculo.modelo + ' ' + self.monto + ' ' + self.estado