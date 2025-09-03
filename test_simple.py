import requests
import json

def test_simple_backend():
    print("Testing Simple Backend...")
    print("=" * 50)
    
    base_url = "http://127.0.0.1:5000"
    
    # Test health endpoint
    print("1. Testing health endpoint:")
    try:
        response = requests.get(f"{base_url}/health")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    print()
    
    # Test trends endpoint
    print("2. Testing trends endpoint:")
    try:
        response = requests.get(f"{base_url}/trends")
        print(f"   Status: {response.status_code}")
        data = response.json()
        
        print(f"   Number of trends: {data.get('count', 0)}")
        print(f"   Source: {data.get('source', 'unknown')}")
        
        if data.get('trends'):
            print(f"   First 5 trends:")
            for i, trend in enumerate(data['trends'][:5], 1):
                print(f"     {i}. {trend}")
        
    except Exception as e:
        print(f"   Error: {e}")
    print()
    
    print("3. Testing multiple requests:")
    for i in range(3):
        try:
            response = requests.get(f"{base_url}/trends")
            data = response.json()
            print(f"   Request {i+1}: {data.get('count', 0)} trends")
        except Exception as e:
            print(f"   Request {i+1} failed: {e}")

if __name__ == "__main__":
    test_simple_backend()