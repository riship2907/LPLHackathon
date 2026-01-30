import pandas as pd
from database import SessionLocal
from models import Trade
from datetime import datetime

EFS_PATH = "/mnt/efs/trades.csv"  # demo mount path


def process_trades():
    df = pd.read_csv(EFS_PATH)
    db = SessionLocal()

    for _, row in df.iterrows():
        if not db.query(Trade).filter(Trade.transaction_id == row['transaction_id']).first():
            trade = Trade(
                transaction_id=row['transaction_id'],
                timestamp=datetime.fromisoformat(row['timestamp']),
                sender_account=row['sender_account'],
                receiver_account=row['receiver_account'],
                amount_ngn=row['amount_ngn'],
                is_fraud=row['is_fraud'],
                fraud_type=row.get('fraud_type', None),
                advisor_id=row.get('advisor_id', None)
            )
            db.add(trade)
    db.commit()
    db.close()
