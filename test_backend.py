import requests
import json

def test_backend():
    base_url = "https://vitara-backend.onrender.com"
    
    # Test home endpoint
    print("Testing home endpoint...")
    response = requests.get(base_url)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test trends endpoint
    print("Testing trends endpoint...")
    response = requests.get(f"{base_url}/trends")
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Number of trends: {data.get('count', len(data.get('trends', [])))}")
        print(f"Trends: {json.dumps(data.get('trends', []), indent=2)}")
        
        if 'error' in data:
            print(f"Warning: Backend error: {data['error']}")
    else:
        print(f"Error: {response.text}")

if __name__ == "__main__":
    test_backend()