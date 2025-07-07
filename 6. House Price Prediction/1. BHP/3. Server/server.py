# 1. Library imports
import uvicorn
from fastapi import FastAPI, HTTPException
from HomePrices import HomePrices
import pickle
import json
import numpy as np
import os

# 2. Create the app object
app = FastAPI()

# Global variables
__model = None
__data_columns = None
__locations = None

def load_saved_artifacts():
    """Load the trained model and data columns"""
    print("Loading saved artifacts...start")
    global __data_columns, __locations, __model
    
    try:
        # Try to load columns data from different possible locations
        columns_file = None
        for path in ["columns.json", "../2. Model/columns.json", "../../2. Model/columns.json"]:
            if os.path.exists(path):
                columns_file = path
                break
        
        if columns_file:
            with open(columns_file, "r") as f:
                __data_columns = json.load(f)['data_columns']
                __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
        else:
            # If columns.json not found, create a basic structure
            print("Warning: columns.json not found, creating basic structure")
            __data_columns = ["total_sqft", "bath", "bhk"]
            __locations = []
        
        # Load the trained model
        model_file = None
        for path in ["banglore_home_prices_model.pickle", "../2. Model/banglore_home_prices_model.pickle"]:
            if os.path.exists(path):
                model_file = path
                break
        
        if model_file:
            with open(model_file, "rb") as f:
                __model = pickle.load(f)
        else:
            raise FileNotFoundError("Model file not found")
        
        print("Loading saved artifacts...done")
        
    except Exception as e:
        print(f"Error loading artifacts: {e}")
        raise e

def get_estimated_price(location, sqft, bath, bhk):
    """Predict house price based on location, sqft, bath, bhk"""
    try:
        if __model is None:
            raise HTTPException(status_code=500, detail="Model not loaded")
        
        # Find location index
        loc_index = -1
        if location.lower() in __data_columns:
            loc_index = __data_columns.index(location.lower())
        
        x = np.zeros(len(__data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1
        
        prediction = __model.predict([x])[0]
        return round(prediction, 2)
    
    except Exception as e:
        print(f"Error in prediction: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

def get_location_names():
    """Get all available location names"""
    return __locations if __locations else []

# Initialize the model when the server starts
load_saved_artifacts()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 5. Get available locations
@app.get('/get_location_names')
def get_location_names_route():
    """Get all available location names"""
    return {'locations': get_location_names()}

# 6. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted house price
@app.post('/predict')
def predict_house_price(data: HomePrices):
    try:
        data = data.model_dump()
        location = data['Location']
        total_sqft = data['total_sqft']
        bhk = data['bhk']
        bath = data['bath']
        
        # Get the estimated price using the trained model
        estimated_price = get_estimated_price(location, total_sqft, bath, bhk)
        
        return {
            'estimated_price': estimated_price,
            'location': location,
            'total_sqft': total_sqft,
            'bhk': bhk,
            'bath': bath
        }
    
    except Exception as e:
        print(f"Error in predict_house_price: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# 7. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn server:app --reload