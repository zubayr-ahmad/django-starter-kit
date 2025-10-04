# Django Starter Kit

A production-ready **Django starter project** with PostgreSQL, JWT authentication, custom user model, email-based password reset, CORS, logging, and Django REST Framework (DRF).
Includes a modern Python dependency setup using **uv** (`pyproject.toml` + `uv.lock`) for fast, reproducible environments.

---

## 🚀 Features

* **Django 5.x** with PostgreSQL support
* **Custom User Model** (email as username)
* **JWT Authentication** (using `djangorestframework-simplejwt`)
* **Password Reset via Email** (with Gmail / SMTP)
* **CORS Setup** (ready for frontend integration)
* **Logging Configuration** (customizable logging setup)
* **uv-based dependency management** (`pyproject.toml` + `uv.lock`)
* Ready-to-use **Django REST Framework** setup

---

## 📦 Requirements

* Python **3.11+**
* PostgreSQL (or SQLite for quick local dev)
* [uv](https://github.com/astral-sh/uv) for dependency management

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/zubayr-ahm/django-starter-kit.git
cd django-starter-kit
```

### 2. Create & activate a virtual environment

(Recommended, but optional since `uv` handles isolated envs)

```bash
uv venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
uv sync
```

This installs all dependencies from `pyproject.toml` and locks exact versions in `uv.lock`.

---

## 🔑 Environment Variables

Create a `.env` file in the project root with the following variables:

```ini
DEBUG=True
SECRET_KEY=your-secret-key-for-django

# Database
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# Email (for password reset)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
DEFAULT_FROM_EMAIL="Project Name <your_email@gmail.com>"
PASSWORD_RESET_FRONTEND_URL="http://localhost:3000/reset-password"
```

---

## 🗄️ Database Setup

Run migrations to set up your database:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

---

## ▶️ Running the Server

Start the dev server:

```bash
python manage.py runserver
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 🔑 Authentication & APIs

* **JWT Authentication** endpoints (provided by DRF SimpleJWT):

  * `POST /api/accounts/login/` – Obtain token (username & password)
  * `POST /api/accounts/token/refresh/` – Refresh access token

* **Password Reset** workflow:

  * `POST /api/accounts/password-reset-request/` – Request reset link (email required)
  * `POST /api/accounts/password-reset-confirm/` – Reset with new password

---

## 🛠️ Dependency Management with uv

* Add a new package:

  ```bash
  uv add <package-name>
  ```

* Remove a package:

  ```bash
  uv remove <package-name>
  ```

* Update dependencies:

  ```bash
  uv sync --upgrade
  ```

---

## 📂 Project Structure

```
django-starter-kit/
│── accounts/          # Custom user & auth
│── core/              # Django settings & URLs
│── pyproject.toml     # Project metadata & dependencies
│── uv.lock            # Locked dependency versions
│── .env.example       # Example environment variables
│── manage.py
```

---

## 🐳 (Optional) Docker Setup

> (Future: Can be extended with `docker-compose` for DB + backend setup.)

---

## 📜 License

MIT License – free to use for personal and commercial projects.
