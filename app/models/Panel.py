from pydantic import BaseModel

class Dimension:
    length: float
    width: float
    depth: float

class Panel(BaseModel):
    brand: str
    dimension: Dimension
    material: str