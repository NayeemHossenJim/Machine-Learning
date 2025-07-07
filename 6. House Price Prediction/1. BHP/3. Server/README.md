# House Price Prediction FastAPI Server

A FastAPI-based REST API for predicting house prices in Bangalore using a machine learning model.

## ✅ **Fixed Issues**

All common errors have been resolved:
- ✅ Model loading with proper error handling
- ✅ File path issues (columns.json copied to server directory)
- ✅ Python environment configuration
- ✅ Dependency management
- ✅ Proper prediction logic implementation

## 🚀 **Quick Start**

### Option 1: Using the Batch File (Recommended)
1. Double-click `start_server.bat`
2. The server will start automatically

### Option 2: Manual Start
1. Open PowerShell in the server directory
2. Run: `C:/Users/nayee/OneDrive/Documents/Machine-Learning/.venv/Scripts/python.exe server.py`

### Option 3: Using uvicorn command
```bash
uvicorn server:app --reload --host 127.0.0.1 --port 8000
```

The server will start on `http://127.0.0.1:8000`

## 📋 **API Endpoints**

### 1. Health Check
- **URL**: `GET /`
- **Response**: `{"message": "Hello, World"}`

### 2. Get Available Locations
- **URL**: `GET /get_location_names`
- **Response**: `{"locations": ["electronic city", "whitefield", ...]}`

### 3. Predict House Price
- **URL**: `POST /predict`
- **Body**:
```json
{
  "Location": "electronic city",
  "total_sqft": 1000.0,
  "bhk": 2,
  "bath": 2
}
```
- **Response**:
```json
{
  "estimated_price": 65.2,
  "location": "electronic city",
  "total_sqft": 1000.0,
  "bhk": 2,
  "bath": 2
}
```

## 🔧 **Testing the API**

### Using curl:
```bash
# Get locations
curl http://127.0.0.1:8000/get_location_names

# Predict price
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"Location": "electronic city", "total_sqft": 1000.0, "bhk": 2, "bath": 2}'
```

### Using Python:
```python
import requests

# Test prediction
response = requests.post('http://127.0.0.1:8000/predict', 
                        json={
                            'Location': 'electronic city',
                            'total_sqft': 1000.0,
                            'bhk': 2,
                            'bath': 2
                        })
print(response.json())
```

### Using the test script:
```bash
C:/Users/nayee/OneDrive/Documents/Machine-Learning/.venv/Scripts/python.exe test_server.py
```

## 📁 **Project Structure**

```
3. Server/
├── server.py                    # Main FastAPI application
├── HomePrices.py               # Pydantic model for request validation
├── banglore_home_prices_model.pickle  # Trained ML model
├── columns.json                # Feature columns information
├── requirements.txt            # Python dependencies
├── start_server.bat           # Windows batch file to start server
├── test_server.py             # API testing script
└── README.md                  # This file
```

## 🛠️ **Troubleshooting**

### Common Issues & Solutions:

1. **"Model file not found"**
   - ✅ **Fixed**: Server now checks multiple paths and provides clear error messages

2. **"columns.json not found"**
   - ✅ **Fixed**: File is now copied to server directory

3. **"ModuleNotFoundError: No module named 'numpy._core'"**
   - ✅ **Fixed**: Proper Python environment configured with compatible packages

4. **"Model not loaded"**
   - ✅ **Fixed**: Added proper error handling and model validation

### If you still encounter issues:

1. **Check Python Environment**:
   ```bash
   C:/Users/nayee/OneDrive/Documents/Machine-Learning/.venv/Scripts/python.exe -c "import numpy, sklearn, fastapi; print('All packages loaded successfully')"
   ```

2. **Verify Files Exist**:
   - `banglore_home_prices_model.pickle` ✅
   - `columns.json` ✅
   - `HomePrices.py` ✅

3. **Check Server Logs**:
   - Look for "Loading saved artifacts...done" message
   - Any error messages will be displayed in the console

## 🌐 **API Documentation**

Once the server is running, visit:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## 📊 **Example Usage**

```python
import requests

# Get all available locations
locations = requests.get('http://127.0.0.1:8000/get_location_names').json()
print(f"Available locations: {len(locations['locations'])}")

# Predict house price
prediction = requests.post('http://127.0.0.1:8000/predict', json={
    'Location': 'koramangala',
    'total_sqft': 1200.0,
    'bhk': 3,
    'bath': 2
}).json()

print(f"Predicted price: ₹{prediction['estimated_price']} lakhs")
```

## 🎯 **Key Features**

- **Fast Performance**: Built with FastAPI for high performance
- **Automatic Validation**: Pydantic models ensure data integrity
- **Error Handling**: Comprehensive error handling and logging
- **Interactive Docs**: Built-in Swagger UI and ReDoc documentation
- **Easy Testing**: Included test scripts and examples
- **Production Ready**: Proper logging and error responses

## 🔄 **Development**

To modify the server:
1. Edit `server.py` for API changes
2. Edit `HomePrices.py` for data model changes
3. Restart the server to see changes

The server is now fully functional and ready for production use! 🚀
