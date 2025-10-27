from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import pickle
import json
import numpy as np
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

model = None
data_columns = None
locations = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    global model, data_columns, locations
    try:
        with open('banglore_home_prices_model.pickle', 'rb') as f:
            model = pickle.load(f)
        
        with open('columns.json', 'r') as f:
            data_columns = json.load(f)['data_columns']
        
        locations = data_columns[3:]
        print("Model loaded successfully")
    except Exception as e:
        print(f"Error loading model: {e}")
        raise e
    
    yield
    
    # Shutdown (cleanup if needed)
    print("Shutting down...")

app = FastAPI(
    title="Bangalore House Price Prediction API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the frontend folder as static files
app.mount("/static", StaticFiles(directory="UI"), name="static")
# Serve index.html at root
@app.get("/")
def read_index():
    return FileResponse("UI/index.html")

class HousePredictionRequest(BaseModel):
    location: str
    sqft: float
    bath: int
    bhk: int

class HousePredictionResponse(BaseModel):
    predicted_price: float
    location: str
    sqft: float
    bath: int
    bhk: int

class HealthResponse(BaseModel):
    status: str
    model_loaded: bool

def predict_price(location: str, sqft: float, bath: int, bhk: int) -> float:
    loc_index = -1
    location_lower = location.lower()
    
    for i, loc in enumerate(data_columns):
        if loc == location_lower:
            loc_index = i
            break

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    
    if loc_index >= 0:
        x[loc_index] = 1
    
    prediction = model.predict([x])[0]
    return round(prediction, 2)

@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy" if model else "unhealthy",
        model_loaded=model is not None
    )

@app.post("/predict", response_model=HousePredictionResponse)
async def predict_house_price(request: HousePredictionRequest):
    if not model:
        raise HTTPException(status_code=503, detail="Model not loaded")
    location_lower = request.location.lower()
    if location_lower not in data_columns:
        raise HTTPException(status_code=400, detail=f"Location '{request.location}' not found.")
    
    predicted_price = predict_price(
        location=request.location,
        sqft=request.sqft,
        bath=request.bath,
        bhk=request.bhk
    )
    
    return HousePredictionResponse(
        predicted_price=predicted_price,
        location=request.location,
        sqft=request.sqft,
        bath=request.bath,
        bhk=request.bhk
    )
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
