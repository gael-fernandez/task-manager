# Task Manager API

Backend construido con FastAPI, SQLAlchemy y SQLite para administrar usuarios y tareas, incluyendo autenticación con JWT y rutas protegidas.

---

## 📌 Descripción

Esta API permite a los usuarios registrarse, iniciar sesión y gestionar sus propias tareas.

Cada usuario puede crear, consultar, actualizar y eliminar tareas, las cuales están asociadas exclusivamente a su cuenta.
La autenticación se realiza mediante JSON Web Tokens (JWT), lo que permite proteger las rutas y asegurar que cada usuario solo acceda a sus propios recursos.

---

## 🛠️ Tecnologías utilizadas

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Passlib (bcrypt)
* JWT (PyJWT)

---

## 🔐 Autenticación

El sistema utiliza JWT para autenticar usuarios.

Flujo:

1. El usuario inicia sesión con `/login`
2. El backend genera un `access_token`
3. El cliente envía el token en el header:

```
Authorization: Bearer <token>
```

4. El backend valida el token y permite acceso a rutas protegidas

---

## 🚀 Endpoints principales

### 👤 Usuarios

* `POST /usuarios` → Crear usuario
* `POST /login` → Iniciar sesión
* `GET /me` → Obtener usuario autenticado
* `PUT /me` → Actualizar usuario
* `DELETE /me` → Eliminar usuario

---

### 📋 Tareas

* `POST /tareas` → Crear tarea
* `GET /tareas` → Listar tareas del usuario
* `PUT /tareas/{id}` → Actualizar tarea
* `DELETE /tareas/{id}` → Eliminar tarea

---

## ⚙️ Instalación y ejecución

1. Clonar repositorio:

```
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO
```

2. Crear entorno virtual:

```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

3. Instalar dependencias:

```
pip install -r requirements.txt
```

4. Crear archivo `.env` en la raíz:

```
SECRET_KEY=tu_clave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Ejecutar servidor:

```
uvicorn app.main:app --reload
```

6. Abrir documentación:

```
http://127.0.0.1:8000/docs
```

---

## 📂 Estructura del proyecto

```
app/
├── models/
├── schemas/
├── routers/
├── utils/
├── database.py
└── main.py
```

---

## 🔒 Seguridad

* Contraseñas hasheadas con bcrypt
* Autenticación con JWT
* Rutas protegidas con Depends()
* Cada usuario solo puede acceder a sus propios datos

---

## 🚀 Mejoras futuras

* Implementación de roles (admin)
* Migración a PostgreSQL
* Deploy en la nube
* Frontend básico
* Tests automatizados

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica de backend orientado a APIs REST y autenticación.
