# 🏠 Bangalore House Price Prediction API

A FastAPI-based web service that predicts house prices in Bangalore using machine learning. The API uses a trained linear regression model to predict prices based on location, square footage, number of bathrooms, and bedrooms.

## 🚀 Features

- **RESTful API** with FastAPI
- **Machine Learning Model** trained on Bangalore house price data
- **Interactive Documentation** with Swagger UI
- **Input Validation** with Pydantic models
- **CORS Support** for web applications
- **Health Check** endpoint
- **Location Listing** endpoint
- **Sample Predictions** for testing

## 📋 Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pandas
- NumPy
- Scikit-learn
- Pydantic

## 🔧 Installation

1. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # On Windows PowerShell
# or
source .venv/bin/activate   # On Linux/Mac
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Make sure you have the model files in the same directory:
   - `banglore_home_prices_model.pickle` (trained model)
   - `columns.json` (feature columns)

## 🏃‍♂️ Running the API

### Method 1: Direct execution (Recommended)
```bash
# Activate virtual environment first
.venv\Scripts\Activate.ps1  # On Windows PowerShell

# Run the application
python main.py
```

### Method 2: Using uvicorn directly
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### ✅ Server Status
Once started, you should see:
- `Model loaded successfully!`
- `Total locations available: 240`
- `Uvicorn running on http://0.0.0.0:8000`

## 📚 API Endpoints

### 1. Root Endpoint
- **GET** `/` - Beautiful homepage with API information and examples

### 2. Health Check
- **GET** `/health` - Check if the API and model are loaded correctly
- Returns: `{"status": "healthy", "model_loaded": true, "total_locations": 240}`

### 3. Get Locations
- **GET** `/locations` - Get all available locations for prediction
- Returns: List of 240+ formatted location names

### 4. Predict Price (Main Endpoint)
- **POST** `/predict` - Predict house price

#### Request Body:
```json
{
    "location": "1st Phase JP Nagar",
    "sqft": 1000,
    "bath": 2,
    "bhk": 2
}
```

#### Response:
```json
{
    "predicted_price": 64.23,
    "location": "1st Phase JP Nagar",
    "sqft": 1000,
    "bath": 2,
    "bhk": 2
}
```

### 5. Sample Predictions
- **GET** `/predict/sample` - Get sample predictions for demonstration
- Returns: Multiple example predictions for popular locations

## 🧪 Testing

You can test the API using several methods:

### 1. Interactive Documentation (Recommended)
Visit `http://localhost:8000/docs` for Swagger UI testing

### 2. Using curl commands
See the examples in the "Example Usage" section below

### 3. Using the built-in sample endpoint
Visit `http://localhost:8000/predict/sample` to see example predictions

## 📖 Interactive Documentation

Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🌐 Example Usage

### Using curl:
```bash
# Health check
curl -X GET "http://localhost:8000/health"

# Get locations
curl -X GET "http://localhost:8000/locations"

# Predict price
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "location": "Indira Nagar",
       "sqft": 1200,
       "bath": 2,
       "bhk": 3
     }'
```

### Using Python requests:
```python
import requests

# Predict price
response = requests.post(
    "http://localhost:8000/predict",
    json={
        "location": "Koramangala",
        "sqft": 1500,
        "bath": 3,
        "bhk": 3
    }
)

prediction = response.json()
print(f"Predicted price: ₹{prediction['predicted_price']} lakhs")
```

## 🏗️ Model Information

The API uses a linear regression model trained on Bangalore house price data with the following features:
- **Location**: Area/neighborhood in Bangalore
- **Square Feet**: Total area of the house
- **Bathrooms**: Number of bathrooms
- **BHK**: Number of bedrooms

The model supports 240+ locations across Bangalore and returns prices in lakhs (Indian currency).

## 🔍 Available Locations

Some popular locations include:
- 1st Phase JP Nagar
- Indira Nagar
- Koramangala
- Whitefield
- BTM Layout
- Banashankari
- Marathahalli
- Electronic City
- Hebbal
- Rajaji Nagar

Use the `/locations` endpoint to get the complete list.

## 🚦 Error Handling

The API includes comprehensive error handling:
- **400 Bad Request**: Invalid input data or unknown location
- **422 Unprocessable Entity**: Invalid data types or missing fields
- **500 Internal Server Error**: Model prediction errors
- **503 Service Unavailable**: Model not loaded

## 📊 Performance

The API is designed for fast predictions with Uvicorn ASGI server:
- Model loading: ~1-2 seconds on startup
- Prediction time: ~1-5ms per request
- Memory usage: ~50-100MB
- **Concurrent requests**: Supported via async FastAPI
- **Auto-reload**: Enabled for development

## 🤝 Contributing

Feel free to contribute by:
1. Adding more features
2. Improving error handling
3. Adding more endpoints
4. Optimizing performance

## 📄 License

This project is for educational purposes.
