from django.db import models

from .mecanico import Mecanico
from .vehiculo import Vehiculo


class Cita(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Confirmada', 'Confirmada'),
        ('Atendida', 'Atendida'),
        ('Cancelada', 'Cancelada'),
    ]

    id = models.BigAutoField(primary_key=True)
    vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.PROTECT, related_name='citas'
    )
    mecanico = models.ForeignKey(
        Mecanico, on_delete=models.PROTECT, related_name='citas'
    )
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Cita #{self.id} - {self.vehiculo.placa} ({self.fecha} {self.hora})"