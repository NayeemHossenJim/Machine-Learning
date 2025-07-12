from fastapi import FastAPI
from HomePrice import HomePriceInput
import pickle

app = FastAPI()

# Load model and encoder
with open("banglore_home_prices_model.pickle","rb") as f:
    model = pickle.load(f)
    
with open("location_encoder.pickle","rb") as f:
    location_encoder = pickle.load(f)

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/{name}')
def get_name(name: str):
    return {'Hello Friend Checking Out haha': f'{name}'}

@app.post('/predict')
def predict_home_price(data: HomePriceInput):
    data = data.model_dump()
    
    try:
        # Encode location string to number
        location_encoded = location_encoder.transform([data['location']])[0]
        total_sqft = data['total_sqft']
        bath = data['bath']
        bhk = data['bhk']
        
        prediction = model.predict([[location_encoded, total_sqft, bath, bhk]])
        prediction = round(prediction[0], 2)
        
        return {'prediction': prediction}
    except ValueError as e:
        return {'error': f'Unknown location: {data["location"]}'}
    except Exception as e:
        return {'error': str(e)}

# uvicorn main:app --reload