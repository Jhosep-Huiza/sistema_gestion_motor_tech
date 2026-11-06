def menu_principal(request):
    return {"menu": [
        ("clientes", "Clientes"), ("vehiculos", "Vehículos"),
        ("mecanicos", "Mecánicos"), ("citas", "Citas"),
        ("diagnosticos", "Diagnósticos"), ("repuestos", "Repuestos"),
        ("ordenes", "Órdenes de servicio"),
    ]}
