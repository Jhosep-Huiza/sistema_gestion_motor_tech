from datetime import date
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import (ClienteForm, VehiculoForm, MecanicoForm, CitaForm,
                    DiagnosticoForm, RepuestoForm, OrdenServicioForm, RegistroForm)
from .models import Cliente, Vehiculo, Mecanico, Cita, Diagnostico, Repuesto, OrdenServicio

ENTIDADES = {
    "clientes": ("Clientes", Cliente, ClienteForm, ("nombres", "apellidos", "dni", "telefono")),
    "vehiculos": ("Vehículos", Vehiculo, VehiculoForm, ("placa", "marca", "modelo")),
    "mecanicos": ("Mecánicos", Mecanico, MecanicoForm, ("nombres", "apellidos", "dni", "especialidad")),
    "citas": ("Citas", Cita, CitaForm, ("motivo", "estado")),
    "diagnosticos": ("Diagnósticos", Diagnostico, DiagnosticoForm, ("descripcion_problema", "causa")),
    "repuestos": ("Repuestos", Repuesto, RepuestoForm, ("codigo", "nombre", "marca")),
    "ordenes": ("Órdenes de servicio", OrdenServicio, OrdenServicioForm, ("descripcion_trabajo", "estado")),
}

@login_required
def dashboard(request):
    return render(request, "control/dashboard.html", {
        "total_clientes": Cliente.objects.count(),
        "total_vehiculos": Vehiculo.objects.count(),
        "total_citas": Cita.objects.count(),
        "total_diagnosticos": Diagnostico.objects.count(),
        "total_ordenes": OrdenServicio.objects.count(),
        "ultimas_ordenes": OrdenServicio.objects.select_related("diagnostico__cita__vehiculo").order_by("-id")[:5],
    })

@login_required
def listado(request, entidad):
    if entidad not in ENTIDADES:
        return redirect("dashboard")
    titulo, modelo, formulario, campos = ENTIDADES[entidad]
    qs = modelo.objects.all()
    if entidad == "vehiculos": qs = qs.select_related("cliente")
    if entidad == "citas": qs = qs.select_related("vehiculo", "mecanico")
    if entidad == "diagnosticos": qs = qs.select_related("cita__vehiculo")
    if entidad == "ordenes": qs = qs.select_related("diagnostico__cita__vehiculo", "repuesto")
    q = request.GET.get("q", "").strip()
    if q:
        filtros = Q()
        for campo in campos: filtros |= Q(**{f"{campo}__icontains": q})
        qs = qs.filter(filtros)
    return render(request, "control/listado.html", {
        "entidad": entidad, "titulo": titulo, "registros": qs,
        "busqueda": q, "modelo": modelo,
    })

@login_required
def crear(request, entidad):
    if entidad not in ENTIDADES: return redirect("dashboard")
    titulo, modelo, formulario, campos = ENTIDADES[entidad]
    form = formulario(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"{titulo[:-1] if titulo.endswith('s') else titulo} registrado correctamente.")
        return redirect("listado", entidad=entidad)
    return render(request, "control/formulario.html", {"form": form, "titulo": f"Registrar {titulo}", "entidad": entidad})

@login_required
def editar(request, entidad, pk):
    if entidad not in ENTIDADES: return redirect("dashboard")
    titulo, modelo, formulario, campos = ENTIDADES[entidad]
    objeto = get_object_or_404(modelo, pk=pk)
    form = formulario(request.POST or None, instance=objeto)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Registro actualizado correctamente.")
        return redirect("listado", entidad=entidad)
    return render(request, "control/formulario.html", {"form": form, "titulo": f"Editar {titulo}", "entidad": entidad})

@login_required
@require_POST
def eliminar(request, entidad, pk):
    if entidad not in ENTIDADES: return redirect("dashboard")
    titulo, modelo, formulario, campos = ENTIDADES[entidad]
    objeto = get_object_or_404(modelo, pk=pk)
    try:
        objeto.delete()
        messages.success(request, "Registro eliminado correctamente.")
    except Exception:
        messages.error(request, "No se puede eliminar: existen registros relacionados.")
    return redirect("listado", entidad=entidad)

@login_required
def reportes(request):
    tipo = request.GET.get("tipo", "citas")
    desde = request.GET.get("desde", "")
    hasta = request.GET.get("hasta", "")
    configuracion = {
        "citas": ("Citas", Cita.objects.select_related("vehiculo__cliente", "mecanico"), "fecha"),
        "diagnosticos": ("Diagnósticos", Diagnostico.objects.select_related("cita__vehiculo__cliente", "cita__mecanico"), "fecha"),
        "ordenes": ("Órdenes de servicio", OrdenServicio.objects.select_related("diagnostico__cita__vehiculo__cliente", "diagnostico__cita__mecanico", "repuesto"), "fecha_inicio"),
    }
    if tipo not in configuracion: tipo = "citas"
    titulo, registros, campo_fecha = configuracion[tipo]
    if desde: registros = registros.filter(**{f"{campo_fecha}__gte": desde})
    if hasta: registros = registros.filter(**{f"{campo_fecha}__lte": hasta})
    return render(request, "control/reportes.html", {
        "tipo": tipo, "titulo": titulo, "registros": registros,
        "desde": desde, "hasta": hasta,
    })

def registro(request):
    if request.user.is_authenticated: return redirect("dashboard")
    form = RegistroForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        usuario = form.save()
        login(request, usuario)
        return redirect("dashboard")
    return render(request, "registration/registro.html", {"form": form})
