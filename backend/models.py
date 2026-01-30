from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String)  # "compliance" or "advisor"
    email = Column(String, nullable=True)

class Trade(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, unique=True, index=True)
    timestamp = Column(DateTime)
    sender_account = Column(Integer)
    receiver_account = Column(Integer)
    amount_ngn = Column(Float)
    is_fraud = Column(Boolean)
    fraud_type = Column(String, nullable=True)
    advisor_id = Column(Integer)
    reviewed_by_compliance = Column(Boolean, default=False)
    review_status = Column(String, default="pending")  # pending, confirmed_fraud, false_positive

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    trade_id = Column(Integer)
    advisor_id = Column(Integer)
    message = Column(String)
    read = Column(Boolean, default=False)
