# 1. Library imports
import uvicorn
from fastapi import FastAPI, HTTPException
from HomePrices import HomePrices
import pickle
import json
import numpy as np

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
    
    # Load columns data
    with open("columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
    
    # Load the trained model
    with open("banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)
    
    print("Loading saved artifacts...done")

def get_estimated_price(location, sqft, bath, bhk):
    """Predict house price based on location, sqft, bath, bhk"""
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

def get_location_names():
    """Get all available location names"""
    return __locations

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

# 7. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn server:app --reload