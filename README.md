# 🏎️ MotorTech Service

> Sistema web integral para la gestión y control de talleres automotrices, desarrollado con Django. Implementa un ecosistema completo de negocio con los siete modelos fundamentales para la operación diaria.

![Django](https://img.shields.io/badge/Django-5.2-092E20?style=flat-square&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-MySQL-003545?style=flat-square&logo=mariadb&logoColor=white)

---

## 📋 Características Principales

- 🔐 **Autenticación y Seguridad:** Inicio de sesión, registro de usuarios, opción de "mantener sesión abierta" y protección CSRF en todos los formularios.
- 📊 **Dashboard Interactivo:** Panel de control con resumen de clientes, vehículos, citas, diagnósticos y órdenes de servicio.
- 🔄 **Gestión Completa (CRUD):** Creación, lectura, actualización, eliminación y búsqueda avanzada para los siete modelos del sistema.
- 📑 **Reportes Dinámicos:** Generación de reportes filtrables por fechas para citas, diagnósticos y órdenes. Incluye botón de impresión optimizado (con opción nativa de "Guardar como PDF" en el navegador).

---

## 🏗️ Arquitectura de Datos

El sistema se basa en los requerimientos del Caso 2, con las siguientes relaciones relacionales:

| Modelo | Relación | Modelo Relacionado |
| :--- | :--- | :--- |
| **Cliente** | `1:N` | Vehículo |
| **Vehículo** | `1:N` | Cita |
| **Mecánico** | `1:N` | Cita |
| **Cita** | `1:N` | Diagnóstico |
| **Diagnóstico** | `1:N` | Orden de Servicio |
| **Repuesto** | `1:N` | Orden de Servicio |

> **Nota:** Cada `OrdenServicio` registra un único tipo de repuesto, tal como establece el alcance del proyecto.

---

## ⚙️ Requisitos del Sistema

- **Python** 3.10 o superior
- **Django** 5.2
- **MariaDB / MySQL** (con `mysqlclient`)
- Entorno virtual (recomendado)

---

## 🚀 Guía de Instalación (Windows)

Sigue estos pasos para poner en marcha el proyecto en tu entorno local:

**1. Crear y activar el entorno virtual:**
```bash
python -m venv .venv
.venv\Scripts\activate

2. Instalar dependencias:

bash
pip install -r requirements.txt
3. Configurar la base de datos en MariaDB/MySQL:
Ejecuta el siguiente comando en tu gestor de base de datos:

sql
CREATE DATABASE motor_tech_service_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
4. Variables de entorno:
Copia el archivo de ejemplo y configura tus credenciales:

bash
copy .env.example .env
(Edita .env y define DB_USER, DB_PASSWORD y DJANGO_SECRET_KEY)

5. Migrar la base de datos y crear el superusuario:

bash
python manage.py migrate
python manage.py createsuperuser
6. Iniciar el servidor:

bash
python manage.py runserver
7. Acceder al sistema:
Abre tu navegador en http://127.0.0.1:8000/

🛡️ Notas sobre Seguridad
Las vistas de gestión requieren estrictamente que el usuario haya iniciado sesión.

Los usuarios registrados a través del formulario público no reciben privilegios administrativos por defecto.

Para un despliegue en producción, es obligatorio configurar:

DEBUG = False

Una SECRET_KEY robusta y privada.

ALLOWED_HOSTS con los dominios permitidos.

Implementación de permisos granulares basados en roles o puestos de trabajo.

Desarrollado para optimizar la operación y el control automotriz.
