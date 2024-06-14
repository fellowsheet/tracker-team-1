from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Literal, Optional

from backend.apps.teams.schemas import Team


statuses = Literal["Владелец", "Менеджер", "Работник"]

class User(BaseModel):
    
    id: int
    telegram_id: int
    name: str
    email: EmailStr
    team: Optional[Team]
    status: statuses
    date_of_joining: date

  
