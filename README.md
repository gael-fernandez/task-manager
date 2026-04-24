# Task Manager API 🚀

A production-ready REST API built with FastAPI for managing personal tasks with secure JWT authentication.

This project demonstrates backend development skills including authentication, database modeling, API design, and cloud deployment.

---

## 📌 Overview

The Task Manager API allows users to:

- Register and authenticate securely using JWT
- Manage their own tasks (create, read, update, delete)
- Access only their own data through protected endpoints
- Interact with a real deployed backend and database

This project was designed as a portfolio-ready backend system following best practices for junior backend developers.

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy (ORM)
- PostgreSQL (Supabase)
- JWT Authentication
- Passlib / Bcrypt
- Render (Backend deployment)

---

## 🔐 Authentication

The API uses JSON Web Tokens (JWT) to secure endpoints.

After login, a token is generated and must be sent in protected requests:
Authorization: Bearer <token>

This ensures that each request is tied to an authenticated user.

---

## 🗄️ Database Design

The project uses PostgreSQL (hosted on Supabase) with the following relationship:
User 1 ─── N Tasks

Each task belongs to a specific user via `usuario_id`.

---

## 📚 Main Endpoints

### Users

| Method | Endpoint | Description |
|---|---|---|
| POST | `/usuarios` | Register user |
| POST | `/login` | Login and get JWT |
| GET | `/me` | Get current user |
| PUT | `/me` | Update user |
| DELETE | `/me` | Delete user |

### Tasks

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tareas` | Get user tasks |
| POST | `/tareas` | Create task |
| PUT | `/tareas/{id}` | Update task |
| DELETE | `/tareas/{id}` | Delete task |

---

## 🔒 Security

- Passwords are hashed using bcrypt
- The backend does not trust client-provided user IDs
- User identity is extracted from JWT tokens
- Task ownership is validated before update/delete operations

Example:

```python
if tarea.usuario_id != usuario_actual.id:
    raise HTTPException(status_code=403)
🌐 Live Deployment

API URL:

https://task-manager-088u.onrender.com

Interactive docs:

https://task-manager-088u.onrender.com/docs

⚠️ Note: The backend is deployed on Render's free tier.
The service may go idle after inactivity, causing the first request to take a few seconds to respond.

⚛️ Frontend

Live application:

https://frontend-task-manager-proyecto-de-p.vercel.app/

Frontend repository:

https://github.com/gael-fernandez/frontend-task-manager-proyecto-de-portafolio
⚙️ Environment Variables

Example .env configuration:

DATABASE_URL=postgresql://...
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
▶️ Run Locally
git clone https://github.com/gael-fernandez/task-manager
cd task-manager
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
🧪 Testing

You can test the API via:

Local Swagger: http://localhost:8000/docs
Production Swagger: https://task-manager-088u.onrender.com/docs
📈 Future Improvements
Automated tests
Refresh tokens
Role-based access
Database migrations (Alembic)
Performance optimization and scaling
👨‍💻 Author

Developed by Gael Fernández as part of a backend / fullstack portfolio project.
