from pydantic import BaseModel

class HomePriceInput(BaseModel):
    location: int
    total_sqft: float
    bath: int
    bhk: int    