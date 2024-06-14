from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Literal, Optional

from backend.apps.users.schemas import User


statuses = Literal["Владелец", "Менеджер", "Работник"]

class Organization(BaseModel):

    id: int
    title: str
    owner: User
    date_of_creation: date

class Team(BaseModel):

    id: int
    title: str
    description: str
    organization: Organization
    date_of_creation: date


