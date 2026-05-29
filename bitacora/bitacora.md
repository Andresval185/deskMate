# Bitácora del Equipo — DeskMate

## Registro de avances, decisiones y obstáculos

---

### 21 de mayo, 2025
**Avances:**
- Initial commit: creación del repositorio en GitHub con README, .gitignore y licencia MIT

**Decisiones tomadas:**
- Se eligió el nombre DeskMate para el sistema
- Se eligió Flask sobre Django por su menor curva de aprendizaje
- Se definieron 4 zonas de escritorios, 6 salas de juntas y 30 cajones de estacionamiento

**Obstáculos:**
- Ninguno

---

### 22 de mayo, 2025
**Avances:**
- Configuración inicial del proyecto: variables de entorno, base de datos MySQL y clave secreta de Flask
- Creación de los modelos de base de datos: usuarios, espacios y reservas
- Creación de las rutas principales: autenticación, escritorios, salas, estacionamiento y mis reservas
- Actualización del README con descripción del proyecto e instrucciones de instalación
- Creación del archivo run.py para correr la aplicación
- Creación de la plantilla base HTML con navbar y sidebar
- Creación de las pantallas de login, registro e inicio
- Agregué el archivo requirements.txt con todas las dependencias

**Decisiones tomadas:**
- Se creó un usuario dedicado `deskmate` en MySQL en lugar de usar root por razones de seguridad
- Se cambió el bloque Jinja2 de `content` a `body` en login y registro para evitar conflicto de bloques duplicados en base.html

**Obstáculos:**
- Trabajar con Kali Linux en una máquina virtual representó varios desafíos técnicos no previstos
- El disco de la máquina virtual se llenó durante la instalación de dependencias, interrumpiendo el proceso y dejando paquetes a medias
- La actualización del kernel de Linux quedó incompleta debido al disco lleno, generando errores al intentar instalar nuevos paquetes
- VS Code no estaba disponible en los repositorios oficiales de Kali y tuvo que instalarse manualmente descargando el paquete .deb desde el sitio oficial
- MySQL no aceptaba conexión con usuario root sin contraseña en versiones nuevas
- El repositorio se dañó en un punto del desarrollo por código duplicado que se acumuló en routes.py al copiar y pegar fragmentos sin reemplazar el contenido anterior
- Solución disco: se movió la máquina virtual al disco D para liberar espacio y se repararon los paquetes con `sudo dpkg --configure -a`
- Solución MySQL: se creó usuario dedicado con permisos específicos sobre la base de datos deskmate
- Solución repositorio: se limpió routes.py manualmente eliminando todo el código duplicado

---

### 27 de mayo, 2025
**Avances:**
- Desarrollo del módulo de reserva de escritorios con mapa visual por zonas
- Actualización de la ruta de escritorios con disponibilidad en tiempo real
- Creación del template de salas de juntas con horarios disponibles
- Actualización de la ruta de salas con validación de conflictos de horario
- Creación del template de estacionamiento con mapa por planta baja y alta
- Actualización de la ruta de estacionamiento con disponibilidad en tiempo real

**Decisiones tomadas:**
- Se decidió mostrar los escritorios como mapa visual por zonas en lugar de lista de tarjetas para hacer la interfaz más intuitiva
- Se dividieron los escritorios en 4 zonas: Zona 1 y 2 con 12 escritorios, Zona 3 y 4 con 10 escritorios

**Obstáculos:**
- Ninguno

---

### 28 de mayo, 2025
**Avances:**
- Agregué el módulo de admin con vista de ocupación diaria y lista de usuarios
- Agregué acceso al panel de administrador en el sidebar
- Limpié los duplicados en routes.py y agregué la ruta de cancelación de reservas
- Creé el módulo de mis reservas con tabla de reservas activas y opción de cancelación

**Decisiones tomadas:**
- Se decidió mostrar solo las últimas 10 reservas en el panel de admin para no sobrecargar la vista
- Se asignó rol de administrador al usuario principal mediante actualización directa en base de datos

**Obstáculos:**
- El archivo routes.py se duplicó nuevamente al agregar nuevas rutas
- Solución: se reemplazó el contenido completo del archivo con la versión limpia

---

### 29 de mayo, 2025
**Avances:**
- Creación del archivo CONTRIBUTING.md con guía de instalación y convenciones de código
- Creación de la bitácora del equipo con registro diario de avances y obstáculos
- Sistema completo y funcional con los 5 módulos operativos

**Decisiones tomadas:**
- Ninguna

**Obstáculos:**
- Ninguno
