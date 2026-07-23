# Gestión de Recursos Humanos API

Sistema completo de API para gestión de recursos humanos desarrollado con **Django REST Framework**, **PostgreSQL** y **JWT**.

El proyecto proporciona una solución integral para administrar empleados, nómina, contratos, vacaciones, capacitaciones y evaluaciones con seguridad profesional, auditoría automática y características avanzadas de exportación.

---

## Arquitectura del Proyecto

### Estructura General

```
Gestion_Recursos_Humanos_API_DJango/
│
├── backend/                    # Configuración principal de Django
│   ├── settings.py            # Configuración del proyecto
│   ├── urls.py                # URLs principales
│   └── wsgi.py
│
├── api/                        # Aplicación principal de la API
│   ├── models.py              # Modelos de datos
│   ├── views.py               # ViewSets
│   ├── serializers.py         # Serializers
│   ├── filters.py             # Filtros avanzados
│   ├── urls.py                # Rutas de la API
│   ├── auth_views.py          # Autenticación JWT
│   ├── renderers.py           # Respuestas personalizadas
│   ├── pagination.py          # Paginación
│   ├── export_utils.py        # Exportación a CSV/Excel
│   ├── export_mixin.py        # Mixin de exportación
│   ├── managers.py            # Managers personalizados
│   ├── middleware.py          # Middleware de usuario
│   ├── signals.py             # Signals de auditoría
│   ├── audit_models.py        # Modelo de auditoría
│   └── apps.py
│
├── .env                        # Variables de entorno
├── manage.py
├── requirements.txt            # Dependencias Python
└── README.md

```

---

## Endpoints Disponibles

### Ejemplo de Flujo CRUD

```
POST   /api/v1/empleados/                    # Crear empleado
GET    /api/v1/empleados/                    # Listar empleados
GET    /api/v1/empleados/:id/                # Obtener empleado
PUT    /api/v1/empleados/:id/                # Actualizar empleado
DELETE /api/v1/empleados/:id/                # Eliminar empleado (Soft Delete)
```

### Endpoints por Módulo

- `/api/v1/generos/`
- `/api/v1/estados_civiles/`
- `/api/v1/tipos_documento/`
- `/api/v1/niveles_cargo/`
- `/api/v1/tipos_contrato/`
- `/api/v1/estados/`
- `/api/v1/modalidades_capacitacion/`
- `/api/v1/tipos_evaluacion/`
- `/api/v1/resultados_evaluacion/`
- `/api/v1/departamentos/`
- `/api/v1/cargos/`
- `/api/v1/empleados/`
- `/api/v1/contratos/`
- `/api/v1/nomina/`
- `/api/v1/vacaciones/`
- `/api/v1/capacitaciones/`
- `/api/v1/evaluaciones/`

**Auditoría:**
- `/api/v1/audit-logs/` - Historial de operaciones

---

## Documentación Swagger

### Acceso a la Documentación

La API incluye documentación interactiva con Swagger UI:

```
http://localhost:8000/swagger/
```

### Características

- Exploración de todos los endpoints
- Pruebas directas de endpoints
- Documentación automática de modelos
- Ejemplos de respuestas
- Autenticación JWT integrada

### Ejemplo de Uso

1. Accede a `http://localhost:8000/swagger/`
2. Busca el endpoint deseado (ej: `/api/v1/empleados/`)
3. Haz clic en "Try it out"
4. Ingresa los parámetros requeridos
5. Ejecuta la prueba

---

## Versionamiento del API

### Versión Actual: v1

Todos los endpoints incluyen el prefijo de versión en la URL:

```
/api/v1/generos/
/api/v1/empleados/
/api/v1/contratos/
```

### Preparación para Futuras Versiones

Si en el futuro necesitas `/api/v2/`, simplemente crea:

```
api/v2/
├── urls.py
├── views.py
├── serializers.py
└── ...
```

---

## Respuestas JSON Estandarizadas

### Estructura

Todas las respuestas siguen un formato consistente:

```json
{
  "success": true,
  "message": "Descripción de la operación",
  "data": { ... }
}
```

### Ejemplos

**Crear Registro (201):**
```json
{
  "success": true,
  "message": "Recurso creado exitosamente",
  "data": {
    "id_generos": 1,
    "nombre": "Masculino",
    "activo": true,
    "creado_en": "2024-06-03T10:30:00Z",
    "usuario_creacion": 1
  }
}
```

**Listar Registros (200):**
```json
{
  "success": true,
  "message": "Solicitud exitosa",
  "data": [
    {
      "id_generos": 1,
      "nombre": "Masculino",
      ...
    }
  ]
}
```

**Error (400/401/500):**
```json
{
  "success": false,
  "message": "Credenciales inválidas",
  "data": null
}
```

---

## Paginación

### Configuración por Defecto

- **Tamaño de página:** 10 registros
- **Máximo permitido:** 100 registros

### Uso

```bash
# Página 1 (por defecto)
GET /api/v1/empleados/

# Página 2
GET /api/v1/empleados/?page=2

# Cambiar tamaño de página
GET /api/v1/empleados/?page=1&page_size=20

# Máximo de 100 registros
GET /api/v1/empleados/?page=1&page_size=50
```

---

## Filtros Avanzados

### Búsqueda por Texto

```bash
# Buscar por nombre
GET /api/v1/empleados/?primer_nombre__icontains=Juan

# Buscar por email
GET /api/v1/empleados/?email=juan@example.com

# Buscar por número de documento
GET /api/v1/empleados/?numero_documento=1234567890
```

### Filtros Numéricos

```bash
# Filtrar por rango de salario
GET /api/v1/cargos/?salario_base_minimo__gte=1000000&salario_base_maximo__lte=5000000
```

### Filtros de Fechas

```bash
# Rango de fechas
GET /api/v1/empleados/?fecha_ingreso_min=2024-01-01&fecha_ingreso_max=2024-12-31
```

### Filtros Booleanos

```bash
# Solo registros activos
GET /api/v1/empleados/?activo=true
```

### Ejemplo Completo

```bash
GET /api/v1/empleados/?primer_nombre__icontains=Juan&activo=true&fecha_ingreso_min=2024-01-01&page=1&page_size=20
```

---

## Ordenamiento Dinámico

### Sintaxis

```bash
# Ordenar ascendente
GET /api/v1/empleados/?ordering=primer_nombre

# Ordenar descendente
GET /api/v1/empleados/?ordering=-fecha_ingreso
```

### Ejemplos

```bash
# Empleados por fecha (más recientes primero)
GET /api/v1/empleados/?ordering=-fecha_ingreso

# Cargos por salario
GET /api/v1/cargos/?ordering=-salario_base_maximo
```

---

## Soft Delete

### ¿Qué es?

Marca registros como eliminados (`activo=false`) sin eliminar físicamente de la BD.

### Comportamiento

```bash
# Al eliminar
DELETE /api/v1/empleados/1/
# El registro se marca: activo=false

# Al listar
GET /api/v1/empleados/
# NO incluye registros con activo=false
```

## Auditoría Automática

### Campos de Auditoría

```json
{
  "usuario_creacion": 1,
  "creado_en": "2024-01-15T10:30:00Z",
  "usuario_modificacion": 2,
  "actualizado_en": "2024-06-03T14:45:00Z"
}
```

### Registro de Operaciones

```bash
# Ver todos tus cambios
GET /api/v1/audit-logs/

# Filtrar por operación
GET /api/v1/audit-logs/?operacion=CREATE

# Filtrar por modelo
GET /api/v1/audit-logs/?modelo=Empleados
```

---

## Autenticación JWT

### Login - Obtener Tokens

```bash
POST /api/v1/auth/login/
Content-Type: application/json

{
  "username": "usuario",
  "password": "contraseña"
}
```

**Respuesta:**
```json
{
  "success": true,
  "message": "Login exitoso",
  "data": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "user": {
      "id": 1,
      "username": "usuario",
      "email": "usuario@example.com"
    }
  }
}
```

### Usar Token en Requests

```bash
GET /api/v1/empleados/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

### Refrescar Token

```bash
POST /api/v1/auth/refresh/
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Tiempos de Expiración

- **Access Token:** 1 hora
- **Refresh Token:** 7 días

---

## Control de Acceso

### Autenticación Requerida

**Todos los endpoints requieren autenticación JWT.**

```bash
# Sin token
GET /api/v1/empleados/
401 Unauthorized

# Con token válido
GET /api/v1/empleados/
Authorization: Bearer <token_valido>
Éxito
```

### Restricción por Usuario

Los logs de auditoría solo muestran cambios del usuario autenticado:

```bash
GET /api/v1/audit-logs/
# Solo devuelve logs donde usuario = usuario_autenticado
```

---

## Relaciones Anidadas (Nested Serializers)

### ¿Qué es?

Muestra datos completos de objetos relacionados.

### Ejemplo: Empleado Completo

```json
{
  "id_empleados": 5,
  "numero_documento": "1234567890",
  "primer_nombre": "Juan",
  "id_generos": {
    "id_generos": 1,
    "nombre": "Masculino"
  },
  "id_cargos": {
    "id_cargos": 3,
    "nombre": "Desarrollador",
    "id_niveles_cargo": {
      "id_niveles_cargo": 2,
      "nombre": "Senior"
    }
  }
}
```

### Modelos con Nested

- **Empleados:** Género, estado civil, documento, cargo, departamento
- **Contratos:** Empleado completo, tipo, estado
- **Nómina:** Empleado, estado
- **Vacaciones:** Empleado, aprobador, estado
- **Capacitaciones:** Empleado, modalidad, estado
- **Evaluaciones:** Empleado, evaluador, tipo, resultado

---

## Exportación de Datos

### Formatos Disponibles

#### CSV

```bash
GET /api/v1/empleados/export/?format=csv
```

#### Excel

```bash
GET /api/v1/empleados/export/?format=excel
```

### Exportar con Filtros

```bash
# Solo empleados activos
GET /api/v1/empleados/export/?format=excel&activo=true

# Por departamento
GET /api/v1/empleados/export/?format=csv&id_departamentos=2

# Rango de fechas
GET /api/v1/empleados/export/?format=excel&fecha_ingreso_min=2024-01-01&fecha_ingreso_max=2024-06-30
```

### Exportar con Ordenamiento

```bash
# Ordenado por nombre
GET /api/v1/empleados/export/?format=csv&ordering=primer_nombre

# Ordenado por fecha descendente
GET /api/v1/empleados/export/?format=excel&ordering=-fecha_ingreso
```

### Todos los Módulos

```bash
GET /api/v1/departamentos/export/?format=csv
GET /api/v1/cargos/export/?format=excel
GET /api/v1/contratos/export/?format=csv
GET /api/v1/nomina/export/?format=excel
GET /api/v1/audit-logs/export/?format=excel
```

---

## Logging de Operaciones

### Registro Automático

Cada operación se registra con:
- Usuario que la realizó
- Tipo (CREATE, UPDATE, DELETE)
- Modelo afectado
- ID y descripción del objeto
- Timestamp

### Consultar Logs

```bash
# Todos tus logs
GET /api/v1/audit-logs/

# Creaciones
GET /api/v1/audit-logs/?operacion=CREATE

# Cambios en Empleados
GET /api/v1/audit-logs/?modelo=Empleados

# Por usuario
GET /api/v1/audit-logs/?usuario=admin

# Rango de fechas
GET /api/v1/audit-logs/?creado_en_min=2024-01-01&creado_en_max=2024-06-30
```

### Exportar Auditoría

```bash
GET /api/v1/audit-logs/export/?format=excel
```

---

## Sistema de Permisos y Usuarios

### ¿Cómo Funciona?

La API implementa un sistema de permisos basado en dos tipos de usuarios:

**Archivo de Configuración:** `api/permissions.py`

### Tipos de Usuarios

####  **Superuser (Administrador)**

| Propiedad | Valor |
|-----------|-------|
| **Username** | `admin` |
| **Email** | `admin@rrhh.com` |
| **Contraseña** | `Admin123456!` |
| **is_staff** |  True |
| **is_superuser** |  True |

**Permisos:**
-  GET (Listar/Ver registros)
-  POST (Crear registros)
-  PUT (Editar registros)
-  DELETE (Eliminar registros)
-  Acceso al panel de administración (`/admin/`)

#### **Usuario Normal**

| Propiedad | Valor |
|-----------|-------|
| **Username** | `empleado` |
| **Email** | `empleado@rrhh.com` |
| **Contraseña** | `Usuario123456!` |
| **is_staff** |  False |
| **is_superuser** |  False |

**Permisos:**
-  GET (Listar/Ver registros)
-  POST (Crear registros)
-  PUT (Editar registros)
-  DELETE (NO puede eliminar)
-  NO acceso al panel de administración

### 📊 Tabla Comparativa

| Operación | Usuario Normal | Superuser |
|-----------|---|---|
| GET (Listar) | Permitido | Permitido |
| POST (Crear) | Permitido | Permitido |
| PUT (Editar) | Permitido | Permitido |
| DELETE (Eliminar) | **Prohibido (403)** | Permitido |
| Admin Panel | Sin acceso | Acceso total |

### Ejemplos de Uso

**Superuser intentando eliminar:**
```bash
DELETE /api/v1/empleados/1/
Authorization: Bearer <token_admin>
204 No Content (Eliminado exitosamente)
```

**Usuario Normal intentando eliminar:**
```bash
DELETE /api/v1/empleados/1/
Authorization: Bearer <token_empleado>
403 Forbidden
{
  "detail": "You do not have permission to perform this action."
}

---

## Gestión de Usuarios

### Crear Usuarios con Script

La forma más simple es usar el script `create_users.py`:

#### Paso 1: Ejecutar el Script

```bash
cd Gestion_Recursos_Humanos_API_DJango
python create_users.py
```

#### Paso 2: Verificar Output

```
Superuser creado:
   Username: admin
   Email: admin@rrhh.com
   Password: Admin123456!
   is_staff: True
   is_superuser: True

Usuario normal creado:
   Username: empleado
   Email: empleado@rrhh.com
   Password: Usuario123456!
   is_staff: False
   is_superuser: False

Usuarios en el sistema:
   Superuser - admin (admin@rrhh.com)
   Normal - empleado (empleado@rrhh.com)
```

#### ¿Qué Hace?

El script `create_users.py`:
1. Crea un superuser automáticamente
2. Crea un usuario normal
3. Asigna contraseñas seguras
4. Configura los permisos correctamente
5. Verifica si ya existen (evita duplicados)
6. Muestra listado de usuarios

### Alternativas para Crear Usuarios

#### Opción 2: Django Admin

1. Ejecutar el servidor: `python manage.py runserver`
2. Acceder a: `http://localhost:8000/admin/`
3. Login con superuser
4. Haz clic en "Users"
5. Crea usuarios desde la interfaz

#### Opción 3: Comando Interactive

```bash
# Crear superuser interactivo
python manage.py createsuperuser

# Crear usuario normal
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_user('username', 'email@example.com', 'password')
```

### Login - Obtener Tokens JWT

Después de crear usuarios, puedes autenticarte:

**Superuser:**
```bash
POST /api/v1/auth/login/
{
  "username": "admin",
  "password": "Admin123456!"
}
```

**Usuario Normal:**
```bash
POST /api/v1/auth/login/
{
  "username": "empleado",
  "password": "Usuario123456!"
}
```

**Respuesta:**
```json
{
  "success": true,
  "message": "Login exitoso",
  "data": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "user": {
      "id": 1,
      "username": "admin",
      "email": "admin@rrhh.com"
    }
  }
}
```

### Usar Token en Requests

Con el token obtenido, acceder a endpoints:

```bash
GET /api/v1/empleados/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

---

## Configuración Local

### Base de Datos PostgreSQL

**Puerto:** `5432`

### API

**Puerto base:** `8000`

---

## Instalación

### 1. Clonar el Proyecto

```bash
git clone https://github.com/juanezzzzz/Gestion_Recursos_Humanos_API_DJango.git
cd Gestion_Recursos_Humanos_API_DJango
```

### 2. Crear Entorno Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno

Crear archivo `.env`:

```env
API_PORT     = # Puerto en el que se ejecutará la API
DEBUG        = # Habilita o deshabilita el modo de depuración (true/false)
DB_NAME      = # Nombre de la base de datos
DB_USER      = # Usuario de acceso a la base de datos
DB_PASSWORD  = # Contraseña del usuario de la base de datos
DB_HOST      = # Dirección IP o nombre del servidor de la base de datos
DB_PORT      = # Puerto de conexión de la base de datos
DB_SCHEMA    = # Nombre del esquema de la base de datos
```

### 5. Ejecutar Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear Usuarios

**Forma Recomendada - Usar el script:**

```bash
python create_users.py
```

Esto crea automáticamente:
- Superuser: `admin` / `Admin123456!`
- Usuario Normal: `empleado` / `Usuario123456!`

**Alternativa - Método interactivo:**

```bash
python manage.py createsuperuser
```

### 7. Ejecutar el Servidor

```bash
python manage.py runserver
```

O especificar puerto:

```bash
python manage.py runserver 0.0.0.0:8000
```

### 8. Acceder a la API

- **API:** http://localhost:8000/api/v1/
- **Swagger:** http://localhost:8000/swagger/
- **Admin:** http://localhost:8000/admin/
- **Usuario Admin:** admin / Admin123456!
- **Usuario Normal:** empleado / Usuario123456!

---

## Swagger UI

### Acceso

```
http://localhost:8000/swagger/
```

### Uso

- Documentación interactiva
- Prueba de endpoints
- Autenticación JWT integrada
- Ejemplos de respuestas

---

## Características del Proyecto

### Seguridad
Autenticación JWT
Control de acceso

### Auditoría
Logging automático
Soft delete
Historial completo
Control de cambios

### Funcionalidad
CRUD automático
Filtros avanzados
Ordenamiento dinámico
Paginación
Relaciones anidadas

### Exportación
CSV
Excel
Con filtros
Auditoría exportable

---

## Tecnología

```
Backend: Django 6.0.5 + DRF
Base de Datos: PostgreSQL
Autenticación: JWT (Simple JWT)
Documentación: Swagger/OpenAPI
Auditoría: Logging automático
Exportación: CSV / Excel
```

---

## Autor

**Juan Valencia**

Proyecto Jobsy - Gestión de Recursos Humanos

---
