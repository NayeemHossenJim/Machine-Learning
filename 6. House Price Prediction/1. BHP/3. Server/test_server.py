import requests
import json

# Test the server
def test_server():
    base_url = "http://127.0.0.1:8000"
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/")
        print("Health check:", response.json())
    except Exception as e:
        print(f"Health check failed: {e}")
    
    # Test locations endpoint
    try:
        response = requests.get(f"{base_url}/get_location_names")
        locations = response.json()
        print(f"Found {len(locations['locations'])} locations")
        print("First 5 locations:", locations['locations'][:5])
    except Exception as e:
        print(f"Locations test failed: {e}")
    
    # Test prediction endpoint
    try:
        test_data = {
            "Location": "electronic city",
            "total_sqft": 1000.0,
            "bhk": 2,
            "bath": 2
        }
        
        response = requests.post(f"{base_url}/predict", json=test_data)
        prediction = response.json()
        print("Prediction result:", prediction)
    except Exception as e:
        print(f"Prediction test failed: {e}")

if __name__ == "__main__":
    test_server()
