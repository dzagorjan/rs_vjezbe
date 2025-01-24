from pydantic import BaseModel
from datetime import datetime


class CCTV_frame(BaseModel):
    identifikator: int
    vrijeme_snimanja: datetime
    koordinate_x_y: tuple[float, float] = (0.00, 0,00)
    
