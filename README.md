# 🚖 Taxi API Project

This is a simple FastAPI-based project for managing taxi data. It connects to a PostgreSQL database and serves an API on port `8000`.

## 🚀 Technologies Used

- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Uvicorn

## 🛠️ Project Structure

taxi_api_project/
├── main.py
├── models/
├── routers/
├── database.py
├── requirements.txt
└── .gitignore

swift
Kopyala
Düzenle

## 🐳 Run with Docker

Make sure PostgreSQL is running via Docker:

```bash
docker run --rm -d \
  --name postgresql \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=Ankara06 \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -p 5432:5432 \
  -v postgresql15_v:/var/lib/postgresql/data \
  postgres:15
Create the database and user:

sql
Kopyala
Düzenle
CREATE DATABASE traindb;
CREATE USER train WITH ENCRYPTED PASSWORD 'Ankara06';
GRANT ALL PRIVILEGES ON DATABASE traindb TO train;
\c traindb
GRANT ALL PRIVILEGES ON SCHEMA public TO train;
🚦 Running the API
Activate your virtual environment and run:

bash
Kopyala
Düzenle
uvicorn main:app --host 0.0.0.0 --port 8000
Then go to: http://localhost:8000/docs
