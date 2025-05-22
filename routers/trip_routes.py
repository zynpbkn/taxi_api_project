from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import TaxiTrip
from database import SessionLocal
from auth import decode_access_token
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# Pydantic modeli
class TaxiTripCreate(BaseModel):
    row_id: str
    VendorID: int
    tpep_pickup_datetime: datetime
    tpep_dropoff_datetime: datetime
    passenger_count: float
    trip_distance: float
    RatecodeID: float
    store_and_fwd_flag: str
    PULocationID: int
    DOLocationID: int
    payment_type: int
    fare_amount: float
    extra: float
    mta_tax: float
    tip_amount: float
    tolls_amount: float
    improvement_surcharge: float
    total_amount: float
    congestion_surcharge: float
    Airport_fee: float

# Veritabanı oturumu alma
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Yolculuk ekleme (sadece doğrulanmış kullanıcılar)
@router.post("/trips")
def create_trip(
    trip: TaxiTripCreate,
    db: Session = Depends(get_db),
    token: str = Depends(decode_access_token)
):
    if token is None:
        raise HTTPException(status_code=401, detail="Kimlik doğrulama gerekli.")

    try:
        new_trip = TaxiTrip(
            row_id=trip.row_id,
            VendorID=trip.VendorID,
            tpep_pickup_datetime=trip.tpep_pickup_datetime,
            tpep_dropoff_datetime=trip.tpep_dropoff_datetime,
            passenger_count=trip.passenger_count,
            trip_distance=trip.trip_distance,
            RatecodeID=trip.RatecodeID,
            store_and_fwd_flag=trip.store_and_fwd_flag,
            PULocationID=trip.PULocationID,
            DOLocationID=trip.DOLocationID,
            payment_type=trip.payment_type,
            fare_amount=trip.fare_amount,
            extra=trip.extra,
            mta_tax=trip.mta_tax,
            tip_amount=trip.tip_amount,
            tolls_amount=trip.tolls_amount,
            improvement_surcharge=trip.improvement_surcharge,
            total_amount=trip.total_amount,
            congestion_surcharge=trip.congestion_surcharge,
            Airport_fee=trip.Airport_fee
        )
        db.add(new_trip)
        db.commit()
        db.refresh(new_trip)
        return {"message": "Yolculuk başarıyla oluşturuldu.", "row_id": new_trip.row_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Yolculuk oluşturulurken hata oluştu: {str(e)}")

# Yolculukları getir (kimlik doğrulama gerektirmez)
@router.get("/trips")
def get_trips(limit: int = 10, db: Session = Depends(get_db)):
    try:
        trips = db.query(TaxiTrip).order_by(TaxiTrip.tpep_pickup_datetime.desc()).limit(limit).all()
        if not trips:
            raise HTTPException(status_code=404, detail="Hiçbir yolculuk kaydı bulunamadı.")
        return trips
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Yolculuklar getirilirken hata oluştu: {str(e)}")
    