# House Price Prediction FastAPI Server

A FastAPI-based REST API for predicting house prices in Bangalore using a machine learning model.

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Automatic Documentation**: Interactive API docs at `/docs` and `/redoc`
- **CORS Support**: Cross-origin requests enabled
- **Input Validation**: Pydantic models for request/response validation
- **Machine Learning**: Predicts house prices based on location, size, bedrooms, and bathrooms

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the server by running:
```bash
python server.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### 1. Health Check
- **URL**: `/health`
- **Method**: GET
- **Description**: Check if the API is running
- **Response**: 
```json
{
  "status": "healthy",
  "message": "House Price Prediction API is running"
}
```

### 2. Get Available Locations
- **URL**: `/get_location_names`
- **Method**: GET
- **Description**: Get all available locations in Bangalore
- **Response**:
```json
{
  "locations": ["electronic city", "whitefield", "koramangala", ...]
}
```

### 3. Predict House Price (GET)
- **URL**: `/predict_home_price`
- **Method**: GET
- **Parameters**:
  - `total_sqft` (float): Total square feet
  - `location` (string): Location name
  - `bhk` (int): Number of bedrooms
  - `bath` (int): Number of bathrooms
- **Example**: `/predict_home_price?total_sqft=1000&location=electronic city&bhk=2&bath=2`

### 4. Predict House Price (POST)
- **URL**: `/predict_home_price`
- **Method**: POST
- **Body**:
```json
{
  "total_sqft": 1000,
  "location": "electronic city",
  "bhk": 2,
  "bath": 2
}
```

**Response** (for both GET and POST):
```json
{
  "estimated_price": 65.2,
  "location": "electronic city",
  "total_sqft": 1000,
  "bhk": 2,
  "bath": 2
}
```

### 5. API Documentation
- **URL**: `/`
- **Method**: GET
- **Description**: Get API documentation and usage information

## Interactive Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: Visit `http://localhost:5000/docs`
- **ReDoc**: Visit `http://localhost:5000/redoc`

## Testing

Run the test script to verify all endpoints:
```bash
python test_api.py
```

## Project Structure

```
3. Server/
├── server.py          # Main FastAPI application
├── requirements.txt   # Python dependencies
├── test_api.py       # API testing script
└── README.md         # This file
```

## Model Files

The server expects the following files in the `../2. Model/` directory:
- `banglore_home_prices_model.pickle` - Trained ML model
- `columns.json` - Feature columns information

## Usage Examples

### Using curl:

```bash
# Health check
curl http://localhost:5000/health

# Get locations
curl http://localhost:5000/get_location_names

# Predict price (GET)
curl "http://localhost:5000/predict_home_price?total_sqft=1000&location=electronic%20city&bhk=2&bath=2"

# Predict price (POST)
curl -X POST "http://localhost:5000/predict_home_price" \
     -H "Content-Type: application/json" \
     -d '{"total_sqft": 1000, "location": "electronic city", "bhk": 2, "bath": 2}'
```

### Using Python requests:

```python
import requests

# Predict price
response = requests.post('http://localhost:5000/predict_home_price', 
                        json={
                            'total_sqft': 1000,
                            'location': 'electronic city',
                            'bhk': 2,
                            'bath': 2
                        })
print(response.json())
```

## Features of FastAPI vs Flask

- **Better Performance**: FastAPI is faster than Flask
- **Automatic Documentation**: Built-in Swagger UI and ReDoc
- **Type Validation**: Automatic request/response validation with Pydantic
- **Modern Python**: Uses Python type hints
- **Async Support**: Built-in support for async/await (though not used in this simple example)
