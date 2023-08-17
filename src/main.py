from fastapi import FastAPI, Header, HTTPException
import datetime
from pydantic import BaseModel, Field

# 正常トークン
correct_token = "correct_token"

# 模擬ユーザーデータ
dummy_user_db = {
    "abcde12345": {"user_id": 12345, "user_name": "Yamada"},
    "fghij67890": {"user_id": 67890, "user_name": "Tanaka"},
}

class Booking(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    
class User(BaseModel):
    user_id: int
    user_name: str = Field(max_length=12)
    
    
class Room(BaseModel):
    room_id: int
    room_name: str = Field(max_length=12)
    capacity: int

app = FastAPI()

@app.get('/')
async def get_root():
    return {'message': 'Hello, world!'}

# ユーザー情報取得API
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, token: str = Header(...)):
    # トークン不正時
    if token != correct_token:
        raise HTTPException(
            status_code=400, detail="token_verification_failed")
    # ユーザー非存在時
    if user_id not in dummy_user_db:
        raise HTTPException(status_code=404, detail="user_not_found")
    return dummy_user_db[user_id]