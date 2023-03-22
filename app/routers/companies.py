from fastapi import APIRouter
from app.models import Company

router = APIRouter()

@router.get("/companies/")
def read_companies():
    return [
        Company(name='Company 1', mission='Mission 1', NUIS='AA01234'),
        Company(name='Company 2', mission='Mission 2', NUIS='AB01234'),
        Company(name='Company 3', mission='Mission 3', NUIS='AC01234'),
        Company(name='Company 4', mission='Mission 4', NUIS='AD01234')
    ]

@router.get("/companies/{NUID}")
def read_companies_by_NUID(NUID: int):
    return {Company(name='Company 1', mission='Mission 1', NUIS='AA01234')}