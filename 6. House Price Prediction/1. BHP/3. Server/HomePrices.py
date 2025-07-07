from pydantic import BaseModel
class HomePrices(BaseModel):
    Location: str
    total_sqft: float
    bhk: int
    bath: int