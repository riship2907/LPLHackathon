from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    role: str
    email: str = None

class UserLogin(BaseModel):
    username: str
    password: str

class TradeBase(BaseModel):
    transaction_id: str
    timestamp: datetime
    sender_account: int
    receiver_account: int
    amount_ngn: float
    is_fraud: bool
    fraud_type: str = None
    advisor_id: int = None

class TradeOut(TradeBase):
    id: int
    review_status: str
