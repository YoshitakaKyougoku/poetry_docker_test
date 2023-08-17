import datetime
from pydantic import BaseModel, Field, ConfigDict

class CreateBooking(BaseModel):
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    
class Booking(CreateBooking):
    booking_id: int
    
    model_config = ConfigDict(orm_mode = True)
class CreateUser(BaseModel):
    user_name: str = Field(max_length=12)

class User(CreateUser):
    user_id: int
    
    model_config = ConfigDict(orm_mode = True)
    
class CreateRoom(BaseModel):
    room_name: str = Field(max_length=12)
    capacity: int

class Room(BaseModel):
    room_id: int
    
    model_config = ConfigDict(orm_mode = True)