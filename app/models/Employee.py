from pydantic import BaseModel
from app.models.Company import Company

class EmployeeInUpdate(BaseModel):
    first_name: str | None
    last_name: str | None
    company: Company | None
    roles: str| None

class Employee(BaseModel):
    id: int
    first_name: str
    last_name: str
    company: Company
    roles: str