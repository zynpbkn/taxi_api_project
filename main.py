from fastapi import FastAPI
from routers import auth_routes, trip_routes
from database import engine
from models import Base

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Rotalar
app.include_router(auth_routes.router)
app.include_router(trip_routes.router)

@app.get("/")
def read_root():
    return {"msg": "Welcome to the Taxi Trip API!"}