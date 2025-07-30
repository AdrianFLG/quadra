# Quadra 🌮

**Quadra** es una aplicación web full-stack diseñada para descubrir, calificar y compartir puestos de comida callejera. Los usuarios pueden geolocalizar, fotografiar y reseñar sus lugares favoritos, creando una guía comunitaria de la mejor comida de la ciudad.

## Características Principales

  * **Registro y Autenticación de Usuarios:** Sistema seguro de registro e inicio de sesión.
  * **Creación de Puestos:** Los usuarios pueden añadir nuevos puestos de comida con nombre, descripción, foto y ubicación.
  * **Calificaciones y Comentarios:** Sistema interactivo para que la comunidad califique (con estrellas) y comente en cada puesto.
  * **Visualización Detallada:** Cada puesto tiene su propia página con toda la información y la lista de reseñas.

-----

## Stack Tecnológico 💻

  * **Backend:** Python con el framework Flask.
  * **Base de Datos:** PostgreSQL para un almacenamiento de datos relacional y robusto.
  * **ORM:** Flask-SQLAlchemy para interactuar con la base de datos desde Python.
  * **Migraciones:** Flask-Migrate (Alembic) para gestionar los cambios en el esquema de la base de datos.
  * **Autenticación:** Flask-Login para el manejo de sesiones de usuario.
  * **Formularios:** Flask-WTF para la creación y validación de formularios.
  * **Frontend:** HTML con plantillas Jinja2 y estilos con Tailwind CSS.

-----

## Paqueterías Necesarias 📦

Para instalar todas las dependencias del proyecto, asegúrate de tener el archivo `requirements.txt` con el siguiente contenido:

```
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-Login
Flask-WTF
psycopg2-binary
python-dotenv
email-validator
```

-----

## Comandos para la Instalación y Ejecución

Sigue estos pasos en tu terminal para poner en marcha el proyecto.

### 1\. **Clona el Repositorio**

```bash
git clone https://github.com/tu-usuario/quadra.git
cd quadra
```

### 2\. **Crea y Activa un Entorno Virtual**

```bash
# Crear el entorno
python3 -m venv venv

# Activar el entorno (en Linux/Mac)
source venv/bin/activate
```

### 3\. **Instala las Dependencias**

```bash
pip install -r requirements.txt
```

### 4\. **Configura la Base de Datos**

  * Asegúrate de tener PostgreSQL instalado y corriendo.
  * Crea un archivo llamado `.env` en la raíz del proyecto y añade la siguiente línea, reemplazando `tu_contraseña` con tu contraseña de PostgreSQL:
    ```
    DATABASE_URL=postgresql://postgres:tu_contraseña@localhost:5432/quadra
    ```
  * Crea la base de datos en PostgreSQL:
    ```bash
    # Entra a la consola de PostgreSQL
    sudo -u postgres psql

    # Ejecuta el comando para crear la base de datos
    CREATE DATABASE quadra;

    # Sal de la consola
    \q
    ```

### 5\. **Crea las Tablas de la Base de Datos**

Estos comandos crearán la estructura de tablas a partir de los modelos de Python.

```bash
# (Asegúrate de que tu entorno virtual esté activado)
export FLASK_APP=aplicacion.py

flask db init
flask db migrate -m "Creacion inicial de la base de datos"
flask db upgrade
```

### 6\. **¡Ejecuta la Aplicación\!**

```bash
flask run
```

¡Listo\! La aplicación estará corriendo en `http://127.0.0.1:5000`.
