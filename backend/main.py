from fastapi import FastAPI, Depends, WebSocket, WebSocketDisconnect
from database import Base, engine, SessionLocal
from crud import create_user, get_user_by_username, get_last_minute_trades, mark_trade_reviewed
from trade_processor import process_trades
from auth import verify_password, create_access_token
from websocket_manager import ConnectionManager
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

Base.metadata.create_all(bind=engine)
manager = ConnectionManager()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    # populate demo users
    db = SessionLocal()
    if not get_user_by_username(db, "advisor1"):
        create_user(db, "advisor1", "password", "advisor", "advisor1@test.com")
        create_user(db, "advisor2", "password", "advisor", "advisor2@test.com")
        create_user(db, "compliance1", "password", "compliance", "compliance@test.com")
    process_trades()
    db.close()

@app.post("/login")
def login(data: dict):
    db = SessionLocal()
    user = get_user_by_username(db, data['username'])
    db.close()
    if user and verify_password(data['password'], user.password_hash):
        token = create_access_token({"sub": user.username, "role": user.role})
        return {"access_token": token, "role": user.role}
    return {"error": "Invalid credentials"}

@app.get("/trades")
def trades(role: str):
    db = SessionLocal()
    trades_list = get_last_minute_trades(db) if role=="compliance" else []
    db.close()
    return trades_list

@app.post("/review_trade")
def review_trade(data: dict):
    db = SessionLocal()
    trade = mark_trade_reviewed(db, data['trade_id'], data['status'])
    db.close()
    return {"trade": trade}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # keep alive
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
