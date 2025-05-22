from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    email = Column(String, nullable=True)

class TaxiTrip(Base):
    __tablename__ = 'trips'
    row_id = Column(String, primary_key=True, index=True)
    VendorID = Column(Integer)
    tpep_pickup_datetime = Column(DateTime)
    tpep_dropoff_datetime = Column(DateTime)
    passenger_count = Column(Float)
    trip_distance = Column(Float)
    RatecodeID = Column(Float)
    store_and_fwd_flag = Column(String)
    PULocationID = Column(Integer)
    DOLocationID = Column(Integer)
    payment_type = Column(Integer)
    fare_amount = Column(Float)
    extra = Column(Float)
    mta_tax = Column(Float)
    tip_amount = Column(Float)
    tolls_amount = Column(Float)
    improvement_surcharge = Column(Float)
    total_amount = Column(Float)
    congestion_surcharge = Column(Float)
    Airport_fee = Column(Float)