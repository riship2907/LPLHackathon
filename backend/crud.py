from sqlalchemy.orm import Session
from models import User, Trade, Notification
from auth import hash_password

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, username, password, role, email=None):
    db_user = User(username=username, password_hash=hash_password(password), role=role, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_trade(db: Session, trade_data: dict):
    trade = Trade(**trade_data)
    db.add(trade)
    db.commit()
    db.refresh(trade)
    return trade

def get_last_minute_trades(db: Session):
    from datetime import datetime, timedelta
    cutoff = datetime.utcnow() - timedelta(minutes=1)
    return db.query(Trade).filter(Trade.timestamp >= cutoff).all()

def mark_trade_reviewed(db: Session, trade_id: int, status: str):
    trade = db.query(Trade).filter(Trade.id==trade_id).first()
    if trade:
        trade.review_status = status
        trade.reviewed_by_compliance = True
        db.commit()
        return trade
    return None
