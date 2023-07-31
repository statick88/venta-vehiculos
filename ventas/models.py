from django.db import models

class Cliente(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dirección = models.CharField(max_length=50)
    teléfono = models.IntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
class Vehículo(models.Model):
    
        marca = models.CharField(max_length=50)
        modelo = models.CharField(max_length=50)
        color = models.CharField(max_length=50)
        anio = models.IntegerField()
        precio = models.FloatField()
        foto = models.ImageField(upload_to='vehículos', null=True)

    
        def __str__(self):
            return self.marca + ' ' + self.modelo

class Venta(models.Model):
        
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehículo = models.ForeignKey(Vehículo, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    costo = models.FloatField(verbose_name='Costo del vehiculo')
    observaciones = models.CharField(max_length=50)
    iva = models.FloatField(choices=[(0.12, '12%')])
    total = models.FloatField()
    descuento = models.FloatField(choices=[(0.1, '10%'), (0.2, '20%'), (0.3, '30%')])  # Add choices for discount percentages

    @property
    def total(self):
        total = self.costo + self.iva - (self.costo * self.descuento)  # Calculate total amount after discount
        return total

    def __str__(self):
        return f"{self.cliente.nombre} {self.cliente.apellido} - {self.vehículo} por el costo tota de: {self.total}"