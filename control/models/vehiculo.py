from django.db import models

from .cliente import Cliente


class Vehiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, related_name='vehiculos'
    )
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    kilometraje = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo}"