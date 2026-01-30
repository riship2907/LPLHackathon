import pandas as pd
from database import SessionLocal
from crud import create_trade
from datetime import datetime
import random

EFS_PATH = "sample_trades.csv"  # demo path

def process_trades():
    df = pd.read_csv(EFS_PATH)
    db = SessionLocal()
    for _, row in df.iterrows():
        trade_data = {
            "transaction_id": row['transaction_id'],
            "timestamp": datetime.strptime(row['timestamp'], "%Y-%m-%d %H:%M:%S"),
            "sender_account": row['sender_account'],
            "receiver_account": row['receiver_account'],
            "amount_ngn": row['amount_ngn'],
            "is_fraud": bool(row['is_fraud']),
            "fraud_type": row.get('fraud_type', None),
            "advisor_id": row.get('advisor_id', random.randint(1,3))  # demo advisor assignment
        }
        create_trade(db, trade_data)
    db.close()
