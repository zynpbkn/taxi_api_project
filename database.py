from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# PostgreSQL bağlantı URL'si – Docker ayarlarına göre güncellendi
DATABASE_URL = "postgresql://train:Ankara06@localhost:5432/traindb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)