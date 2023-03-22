from typing import List
from pydantic import BaseModel
from enum import Enum
from app.models.Panel import Panel

class Orientation(Enum):
    N = 'North'
    E = 'East'
    W = 'West'
    S = 'South'
    NW = 'North West'
    NE = 'North East'
    SW = 'South West'
    SE = 'South East'

class FarmInCreate(BaseModel):
    location: str
    area: str
    output: str
    panels: List[Panel] = []
    landscape: str
    orientation: Orientation

class FarmInUpdate(BaseModel):
    location: str | None
    area: str | None
    output: str | None
    panels: List[Panel] | None
    landscape: str | None
    orientation: Orientation | None

class Farm(BaseModel):
    location: str
    area: str
    output: str
    panels: List[Panel] = []
    no_panels: int = len(panels)
    landscape: str
    orientation: Orientation