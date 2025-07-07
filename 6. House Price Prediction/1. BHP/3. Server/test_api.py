import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:5000"

def test_health():
    """Test the health endpoint"""
    print("Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50)

def test_get_locations():
    """Test the get locations endpoint"""
    print("Testing get locations endpoint...")
    response = requests.get(f"{BASE_URL}/get_location_names")
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Number of locations: {len(data['locations'])}")
    print(f"First 5 locations: {data['locations'][:5]}")
    print("-" * 50)

def test_predict_price_get():
    """Test the predict price endpoint using GET method"""
    print("Testing predict price endpoint (GET)...")
    params = {
        'total_sqft': 1000,
        'location': 'electronic city',
        'bhk': 2,
        'bath': 2
    }
    response = requests.get(f"{BASE_URL}/predict_home_price", params=params)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50)

def test_predict_price_post():
    """Test the predict price endpoint using POST method"""
    print("Testing predict price endpoint (POST)...")
    data = {
        'total_sqft': 1200,
        'location': 'whitefield',
        'bhk': 3,
        'bath': 2
    }
    response = requests.post(f"{BASE_URL}/predict_home_price", json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50)

def test_home():
    """Test the home endpoint"""
    print("Testing home endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print("-" * 50)

if __name__ == "__main__":
    print("Testing House Price Prediction API")
    print("=" * 60)
    
    try:
        test_health()
        test_get_locations()
        test_predict_price_get()
        test_predict_price_post()
        test_home()
        print("All tests completed successfully!")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API server.")
        print("Make sure the server is running on http://localhost:5000")
    except Exception as e:
        print(f"Error occurred: {e}")
