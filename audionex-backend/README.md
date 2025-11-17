# Audionex Backend

This directory contains the FastAPI application that serves as the backend for the Audionex platform.

## ⚙️ Local Development

Follow these steps to run the backend application on your local machine.

### 1. Prerequisites

- Python 3.9+
- `virtualenv` (or another environment manager)

### 2. Setup

1.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**

    Copy the example `.env` file and update it with your local database and Redis connection strings. In a real project, you would need to have PostgreSQL and Redis running locally (e.g., via Docker).

    ```bash
    cp .env.example .env
    # Edit .env with your local settings
    ```
    *Note: A starter `.env` is already provided.*

### 3. Running the Application

Once the setup is complete, you can run the FastAPI application using `uvicorn`:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## 📦 API Structure

The API is built using FastAPI and follows a structured layout:

- **`main.py`**: The entry point for the FastAPI application.
- **`api/v1/`**: Contains the API endpoints, organized by version.
- **`core/`**: Core settings and configuration management.
- **`db/`**: SQLAlchemy models and database session management.
- **`schemas/`**: Pydantic schemas for request/response validation and serialization.
