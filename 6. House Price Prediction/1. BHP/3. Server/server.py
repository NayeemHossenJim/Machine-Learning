# 1. Library imports
import uvicorn
from fastapi import FastAPI
from HomePrices import HomePrices
import pickle
# 2. Create the app object
app = FastAPI()
pickle_in = open("banglore_home_prices_model.pickle","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted house price
@app.post('/predict')
def predict_house_price(data: HomePrices):
    data = data.model_dump()
    location = data['Location']
    total_sqft = data['total_sqft']
    bhk = data['bhk']
    bath = data['bath']
    
    # You'll need to implement the actual prediction logic based on your model
    # This is a placeholder - replace with your actual prediction logic
    prediction = classifier.predict([[total_sqft, bath, bhk]])  # Adjust based on your model's expected input
    
    return {
        'estimated_price': float(prediction[0]),
        'location': location,
        'total_sqft': total_sqft,
        'bhk': bhk,
        'bath': bath
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload