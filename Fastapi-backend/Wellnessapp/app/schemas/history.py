from decimal import Decimal
from pydantic import BaseModel
from datetime import datetime


# 요청 본문으로 받을 데이터 모델 정의
class HistoryCreateRequest(BaseModel):
    user_id: int
    category_id: int
    meal_type_id: int
    image_url: str
    date: datetime
      
class MealResponse(BaseModel):
    history_id: int
    meal_type_name: str
    category_name: str
    food_kcal: Decimal




class HistoryBase(BaseModel):
    user_id: int
    category_id: int
    meal_type_id: int
    image_url: str
    date: datetime

class HistoryCreate(HistoryBase):
    pass

class HistoryUpdate(HistoryBase):
    pass

class HistoryInDB(HistoryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True




