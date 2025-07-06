from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import json
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Global variables to store model and data columns
__model = None
__data_columns = None
__locations = None

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

@app.route('/get_location_names', methods=['GET'])
def get_location_names_route():
    """
    API endpoint to get all available locations
    """
    response = jsonify({
        'locations': get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    """
    API endpoint to predict house price
    Expected parameters: total_sqft, location, bhk, bath
    """
    if request.method == 'POST':
        data = request.get_json()
        total_sqft = float(data['total_sqft'])
        location = data['location']
        bhk = int(data['bhk'])
        bath = int(data['bath'])
    else:  # GET request
        total_sqft = float(request.args.get('total_sqft'))
        location = request.args.get('location')
        bhk = int(request.args.get('bhk'))
        bath = int(request.args.get('bath'))

    estimated_price = get_estimated_price(location, total_sqft, bhk, bath)
    
    response = jsonify({
        'estimated_price': estimated_price,
        'location': location,
        'total_sqft': total_sqft,
        'bhk': bhk,
        'bath': bath
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint
    """
    response = jsonify({
        'status': 'healthy',
        'message': 'House Price Prediction API is running'
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/', methods=['GET'])
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
    
    response = jsonify(api_docs)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    load_saved_artifacts()
    app.run(host='0.0.0.0', port=5000, debug=True)