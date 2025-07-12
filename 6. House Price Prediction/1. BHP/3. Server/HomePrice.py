from pydantic import BaseModel

class HomePriceInput(BaseModel):
    location: str
    total_sqft: float
    bath: int
    bhk: int    