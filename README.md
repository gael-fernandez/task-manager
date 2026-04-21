# Task Manager API

Backend built with FastAPI, SQLAlchemy, and SQLite to manage users and tasks, including JWT authentication and protected routes.

---

## 📌 Description

This API allows users to register, log in, and manage their own tasks.

Each user can create, read, update, and delete tasks that are exclusively associated with their account.
Authentication is handled using JSON Web Tokens (JWT), ensuring that routes are protected and users can only access their own resources.

---

## 🛠️ Technologies

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Passlib (bcrypt)
* JWT (PyJWT)

---

## 🔐 Authentication

The system uses JWT for user authentication.

Flow:

1. The user logs in via `/login`
2. The backend generates an `access_token`
3. The client sends the token in the header:

```
Authorization: Bearer <token>
```

4. The backend validates the token and grants access to protected routes

---

## 🚀 Main Endpoints

### 👤 Users

* `POST /usuarios` → Create user
* `POST /login` → Log in
* `GET /me` → Get authenticated user
* `PUT /me` → Update user
* `DELETE /me` → Delete user

---

### 📋 Tasks

* `POST /tareas` → Create task
* `GET /tareas` → List user tasks
* `PUT /tareas/{id}` → Update task
* `DELETE /tareas/{id}` → Delete task

---

## ⚙️ Installation & Setup

1. Clone repository:

```
git clone https://github.com/gael-fernandez/task-manager
cd task-manager
```

2. Create virtual environment:

```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Create `.env` file in the root:

```
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Run the server:

```
uvicorn app.main:app --reload
```

6. Open API docs:

```
http://127.0.0.1:8000/docs
```

---

## 📂 Project Structure

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

## 🔒 Security

* Passwords hashed with bcrypt
* JWT-based authentication
* Protected routes using Depends()
* Users can only access their own data

---

## 🚀 Future Improvements

* Role-based access (admin)
* Migration to PostgreSQL
* Cloud deployment
* Basic frontend
* Automated tests

---

## 👨‍💻 Author

Backend project focused on REST APIs and authentication systems.
