from typing import List
from fastapi import FastAPI, Header, HTTPException, Depends
import datetime
from pydantic import BaseModel, Field
from sql_app import crud, models, schemas
from sql_app.database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

# 正常トークン
correct_token = "correct_token"

# 模擬ユーザーデータ
dummy_user_db = {
    "abcde12345": {"user_id": 12345, "user_name": "Yamada"},
    "fghij67890": {"user_id": 67890, "user_name": "Tanaka"},
}

app = FastAPI()

# CORS設定を行う
origins = ["http://localhost:3000"]  # 許可するオリジンを指定

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可
    allow_headers=["*"],  # すべてのヘッダーを許可
    allow_credentials=True,  # クレデンシャル情報の送信を許可（必要に応じて）
    expose_headers=["Content-Disposition"],  # クライアントに公開するヘッダーを指定（必要に応じて）
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
async def get_root():
    return {'message': 'Hello, world!'}

# Read
# ユーザー一覧取得API
@app.get("/users", response_model=List[schemas.User])
async def read_all_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_user(db, skip=skip, limit=limit)
    

# ユーザー情報取得API
@app.get("/users/{user_id}", response_model=schemas.User)
async def get_user(user_id: str ,db: Session = Depends(get_db)):
    user_id = int(user_id)
    return crud.get_user(db, user_id=user_id)

# 会議室一覧取得API
@app.get("/rooms", response_model=List[schemas.Room])
async def read_all_room(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_room(db, skip=skip, limit=limit)

# 予約一覧取得API
@app.get("/bookings", response_model=List[schemas.Booking])
async def read_all_booking(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_booking(db, skip=skip, limit=limit)

# Create
# ユーザー登録API
@app.post("/users", response_model=schemas.User)
async def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# 会議室登録API
@app.post("/rooms", response_model=schemas.Room)
async def create_room(room: schemas.CreateRoom, db: Session = Depends(get_db)):
    return crud.create_room(db=db, room=room)

# 予約登録API
@app.post("/bookings", response_model=schemas.Booking)
async def create_booking(booking: schemas.CreateBooking, db: Session = Depends(get_db)):
    return crud.create_booking(db=db, booking=booking)

# Update
# ユーザー名更新API
@app.post("/users/update", response_model=schemas.User)
async def update_user_name(user: schemas.User, db: Session = Depends(get_db)):
    return crud.update_user_name(db=db, user=user)

# Delete
# ユーザー削除API
@app.post("/users/delete", response_model=schemas.User)
async def delete_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.delete_user(db=db, user=user)