from pydantic import BaseModel, Field

class BaseCar(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int = Field(ge=1960, le=2025)
    cijena: float = Field(ge=0)
    boja: str

    
class CarResponse(BaseCar):
    id: int

class CarWithPdv(CarResponse):
    cijena_pdv: float