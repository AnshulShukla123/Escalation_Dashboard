#!/usr/bin/env python3
"""Simple Flask test script to debug form submission issues."""

import requests
import sys

def test_routes():
    base_url = "http://127.0.0.1:5003"
    
    # Test 1: Simple GET request to home
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        print(f"GET / - Status: {response.status_code}")
        if response.status_code == 200:
            print("✓ Home route is working")
        else:
            print(f"✗ Home route failed with status {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"✗ GET / failed: {e}")
        return False
    
    # Test 2: Simple test route
    try:
        response = requests.post(f"{base_url}/simple_test", 
                               data={"test": "value"}, 
                               timeout=5)
        print(f"POST /simple_test - Status: {response.status_code}")
        print(f"Response: {response.text}")
        if response.status_code == 200:
            print("✓ Simple test route is working")
        else:
            print(f"✗ Simple test route failed with status {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"✗ POST /simple_test failed: {e}")
        return False
        
    # Test 3: Submit route (should work if login is disabled)
    try:
        test_data = {
            'escalation_id': 'TEST123',
            'customer': 'Test Customer',
            'problem_title': 'Test Problem',
            'engineer': 'testuser'
        }
        response = requests.post(f"{base_url}/submit", 
                               data=test_data, 
                               timeout=10)
        print(f"POST /submit - Status: {response.status_code}")
        print(f"Response length: {len(response.text)} chars")
        if response.status_code in [200, 302]:  # 302 is redirect
            print("✓ Submit route is accessible")
        else:
            print(f"✗ Submit route failed with status {response.status_code}")
            print(f"Response preview: {response.text[:200]}...")
    except requests.exceptions.RequestException as e:
        print(f"✗ POST /submit failed: {e}")
        return False
        
    return True

if __name__ == "__main__":
    print("Testing Flask routes...")
    success = test_routes()
    sys.exit(0 if success else 1)