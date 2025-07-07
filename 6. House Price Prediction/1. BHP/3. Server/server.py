from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json
import numpy as np
import os
import uvicorn

app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting house prices in Bangalore",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables to store model and data columns
__model = None
__data_columns = None
__locations = None

# Pydantic models for request/response
class PredictionRequest(BaseModel):
    total_sqft: float
    location: str
    bhk: int
    bath: int

class PredictionResponse(BaseModel):
    estimated_price: float
    location: str
    total_sqft: float
    bhk: int
    bath: int

class LocationsResponse(BaseModel):
    locations: list

class HealthResponse(BaseModel):
    status: str
    message: str

def get_estimated_price(location, sqft, bhk, bath):
    """
    Predict house price based on location, square feet, bedrooms, and bathrooms
    """
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    """
    Load the trained model and data columns from saved files
    """
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    # Get the path to the model directory
    model_path = os.path.join(os.path.dirname(__file__), '..', '2. Model')
    
    # Load columns data
    with open(os.path.join(model_path, 'columns.json'), 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # First 3 columns are sqft, bath, bhk

    # Load the trained model
    with open(os.path.join(model_path, 'banglore_home_prices_model.pickle'), 'rb') as f:
        __model = pickle.load(f)
    
    print("Loading saved artifacts...done")

def get_location_names():
    """
    Get all available location names
    """
    return __locations

def get_data_columns():
    """
    Get all data columns
    """
    return __data_columns

@app.get('/get_location_names', response_model=LocationsResponse)
def get_location_names_route():
    """
    API endpoint to get all available locations
    """
    return LocationsResponse(locations=get_location_names())

@app.post('/predict_home_price', response_model=PredictionResponse)
def predict_home_price_post(request: PredictionRequest):
    """
    API endpoint to predict house price using POST method
    """
    estimated_price = get_estimated_price(request.location, request.total_sqft, request.bhk, request.bath)
    
    return PredictionResponse(
        estimated_price=estimated_price,
        location=request.location,
        total_sqft=request.total_sqft,
        bhk=request.bhk,
        bath=request.bath
    )

@app.get('/predict_home_price', response_model=PredictionResponse)
def predict_home_price_get(total_sqft: float, location: str, bhk: int, bath: int):
    """
    API endpoint to predict house price using GET method
    """
    estimated_price = get_estimated_price(location, total_sqft, bhk, bath)
    
    return PredictionResponse(
        estimated_price=estimated_price,
        location=location,
        total_sqft=total_sqft,
        bhk=bhk,
        bath=bath
    )

@app.get('/health', response_model=HealthResponse)
def health_check():
    """
    Health check endpoint
    """
    return HealthResponse(
        status='healthy',
        message='House Price Prediction API is running'
    )

@app.get('/')
def home():
    """
    Home endpoint with API documentation
    """
    api_docs = {
        'message': 'Welcome to House Price Prediction API',
        'endpoints': {
            '/health': 'GET - Health check',
            '/get_location_names': 'GET - Get all available locations',
            '/predict_home_price': 'GET/POST - Predict house price',
        },
        'prediction_parameters': {
            'total_sqft': 'Total square feet (number)',
            'location': 'Location name (string)',
            'bhk': 'Number of bedrooms (integer)',
            'bath': 'Number of bathrooms (integer)'
        },
        'example_request': {
            'url': '/predict_home_price?total_sqft=1000&location=electronic city&bhk=2&bath=2',
            'method': 'GET'
        }
    }
    
    return api_docs

if __name__ == "__main__":
    print("Starting Python FastAPI Server For Home Price Prediction...")
    load_saved_artifacts()
    uvicorn.run(app, host="0.0.0.0", port=5000)