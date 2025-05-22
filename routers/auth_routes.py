from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import User
from database import SessionLocal
from auth import hash_password, verify_password, create_access_token, decode_access_token

router = APIRouter()

# Pydantic modelleri
class UserCreate(BaseModel):
    username: str
    password: str
    email: str = None

class UserLogin(BaseModel):
    username: str
    password: str

# Veritabanı oturumu alma
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Kullanıcı kayıt
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    try:
        hashed_password = hash_password(user.password)
        new_user = User(username=user.username, password_hash=hashed_password, email=user.email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"msg": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error occurred while registering user")

# Kullanıcı giriş
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}