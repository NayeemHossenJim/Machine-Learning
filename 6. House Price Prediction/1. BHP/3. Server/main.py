import uvicorn
from fastapi import FastAPI
from HomePrice import HomePriceInput
import pickle

app = FastAPI()
pickle_in = open("banglore_home_prices_model.pickle","rb")
Model=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.get('/{name}')
def get_name(name: str):
    return {'Hello Friend Checking Out haha': f'{name}'}

@app.post('/predict')
def Predict_HomePrice(data:HomePriceInput):
    data = data.model_dump()
    location = data['location']
    total_sqft = data['total_sqft']
    bath = data['bath']
    bhk = data['bhk']
    prediction = Model.predict([[location, total_sqft, bath, bhk]])
    prediction = round(prediction[0], 2)
    return {'prediction': prediction}

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload