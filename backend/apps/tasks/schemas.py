from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Literal, Optional

from backend.apps.users.schemas import User


conditions = Literal["Выполнено", "На рассмотрении", "В процессе", "В ожидании"]
priorities = Literal["Высокий", "Средний", "Низкий"]

class Task(BaseModel):

    id: int
    title: str
    description: Optional[str]
    responsible_person: User
    tags: List[str]
    condition: conditions
    priority: priorities
    date_of_creation: date
    deadline_date: date





