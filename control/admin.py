from django.contrib import admin
from .models import Cliente, Vehiculo, Mecanico, Cita, Diagnostico, Repuesto, OrdenServicio

admin.site.register([Cliente, Vehiculo, Mecanico, Cita, Diagnostico, Repuesto, OrdenServicio])
