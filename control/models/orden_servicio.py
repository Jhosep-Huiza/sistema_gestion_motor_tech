from decimal import Decimal

from django.db import models

from .diagnostico import Diagnostico
from .repuesto import Repuesto


class OrdenServicio(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Finalizada', 'Finalizada'),
    ]

    id = models.BigAutoField(primary_key=True)
    diagnostico = models.ForeignKey(
        Diagnostico, on_delete=models.PROTECT, related_name='ordenes'
    )
    repuesto = models.ForeignKey(
        Repuesto, on_delete=models.PROTECT, related_name='ordenes'
    )
    descripcion_trabajo = models.TextField()
    cantidad_repuesto = models.PositiveIntegerField()
    costo_mano_obra = models.DecimalField(max_digits=10, decimal_places=2)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_inicio = models.DateField()
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')

    def save(self, *args, **kwargs):
        # costo_total = mano de obra + (precio del repuesto x cantidad)
        self.costo_total = self.costo_mano_obra + (
            self.repuesto.precio * Decimal(self.cantidad_repuesto)
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Orden #{self.id} - {self.estado}"