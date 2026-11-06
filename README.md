# MotorTech Service

Sistema web Django para la gestión de un taller automotriz. Implementa los siete modelos de negocio solicitados en el Caso 2: Cliente, Vehiculo, Mecanico, Cita, Diagnostico, Repuesto y OrdenServicio.

## Requisitos
- Python 3.10 o superior
- Django 5.2
- MariaDB / MySQL
- mysqlclient

## Instalación en Windows
1. Crear y activar un entorno virtual:
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Crear una base de datos MariaDB:
   ```sql
   CREATE DATABASE motor_tech_service_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
4. Copiar `.env.example` como `.env` y configurar `DB_USER`, `DB_PASSWORD` y `DJANGO_SECRET_KEY`.
5. Ejecutar migraciones y crear usuario administrador:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. Iniciar:
   ```bash
   python manage.py runserver
   ```
7. Abrir `http://127.0.0.1:8000/`.

## Funciones
- Autenticación, registro de usuarios y opción de mantener sesión.
- Dashboard de clientes, vehículos, citas, diagnósticos y órdenes.
- CRUD y búsqueda de los siete modelos.
- Reportes filtrables de citas, diagnósticos y órdenes. El botón Imprimir permite imprimir o seleccionar «Guardar como PDF» en el navegador.

## Modelos y relaciones
- Cliente 1:N Vehiculo
- Vehiculo 1:N Cita
- Mecanico 1:N Cita
- Cita 1:N Diagnostico
- Diagnostico 1:N OrdenServicio
- Repuesto 1:N OrdenServicio

Cada OrdenServicio registra un único tipo de repuesto, tal como establece el alcance del Caso 2.

## Seguridad
Los formularios POST incluyen CSRF, las vistas de gestión requieren inicio de sesión y los usuarios registrados no reciben privilegios administrativos. Para producción, configura `DEBUG=False`, una clave secreta propia, hosts permitidos y permisos por puesto.
