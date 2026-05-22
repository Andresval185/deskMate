# DeskMate 🏢

**Sistema de Reservas de Espacios de Trabajo — DataVault Analytics**

DeskMate es un sistema web interno desarrollado con tecnologías de código abierto que permite a los colaboradores de DataVault Analytics reservar con anticipación su espacio de trabajo antes de ir a la oficina. El sistema gestiona tres tipos de recursos: escritorios individuales, salas de juntas y cajones de estacionamiento.

---

## ¿Por qué DeskMate?

DataVault Analytics opera bajo un modelo de trabajo híbrido donde los colaboradores asisten a la oficina ciertos días a la semana. Con 100 empleados y oficinas de capacidad limitada, se generaba un problema recurrente: los empleados llegaban y no encontraban lugar disponible para trabajar ni dónde estacionarse. DeskMate resuelve este problema permitiendo reservar espacios con anticipación.

---

## Stack tecnológico

| Tecnología | Uso | Licencia |
|---|---|---|
| Python 3.11 | Lenguaje principal | PSF License |
| Flask 3.x | Framework web | BSD 3-Clause |
| MySQL 8.x | Base de datos | GPL 2.0 |
| SQLAlchemy | ORM | MIT |
| Bootstrap 5 | Frontend | MIT |
| Docker | Contenedores | Apache 2.0 |
| Git + GitHub | Control de versiones | GPL 2.0 |

---

## Funcionalidades

- 🔐 Autenticación con roles (colaborador y administrador)
- 🖥️ Reserva de escritorios individuales
- 🏛️ Reserva de salas de juntas
- 🚗 Reserva de cajones de estacionamiento
- 📊 Panel de administrador con reporte de ocupación

---

## Instalación

### Requisitos previos
- Python 3.11+
- MySQL 8.x
- Git

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/Andresval185/deskMate.git
cd deskMate

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales de MySQL

# 5. Crear la base de datos
mysql -u root -p -e "CREATE DATABASE deskmate;"

# 6. Correr la aplicación
python run.py
```

La aplicación estará disponible en `http://localhost:5000`

---

*Proyecto Final — Sistemas y Lenguajes de Código Abierto · Universidad Panamericana · 2025*