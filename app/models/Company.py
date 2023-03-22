from typing import List
from pydantic import BaseModel
from app.models.Employee import Employee

class Company(BaseModel):
    name: str
    mission: str
    NUIS: str
    employees: List[Employee] = []