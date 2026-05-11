#!/usr/bin/env python3
"""
Test 4x2 Grid Layout - 4 fields per row, 2 rows total
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_4x2_grid():
    """Test 4x2 grid layout format"""
    print("🧪 Testing 4x2 Grid Layout...\n")
    
    WEBEX_BOT_TOKEN = os.getenv("WEBEX_BOT_TOKEN")
    WEBEX_ROOM_ID = os.getenv("WEBEX_ROOM_ID")
    HOST_URL = os.getenv("HOST_URL", "localhost:5000")
    
    if not all([WEBEX_BOT_TOKEN, WEBEX_ROOM_ID]):
        print("❌ Missing Webex credentials")
        return
    
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {WEBEX_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Test data showing the 4x2 grid
    data = {
        "id": 789,
        "customer": "Toyota4",
        "version": "17.12.5",
        "bug_id": "CSCwr46982",
        "component": "Client Join in SDA",
        "severity": "CAP",
        "severity_remarks": "Deployment change: from non-SDA to SDA",
        "de_mgr": "Hari",
        "primary_poc": "Srihari",
        "contributors": "None",
        "cross_teams": "Location",
        "remarks": "Testing 4x2 grid layout with all fields organized in two rows of four columns each.",
        "url": f"http://{HOST_URL}/edit/789"
    }
    
    print("📊 4x2 Grid Layout:")
    print("Row 1: Customer | Version | Bug ID | Component")
    print(f"       {data['customer']:<10} | {data['version']:<8} | {data['bug_id']:<12} | {data['component']}")
    print("\nRow 2: Severity | DE Mgr | Primary PoC | Contributors") 
    print(f"       {data['severity']:<8} | {data['de_mgr']:<7} | {data['primary_poc']:<12} | {data['contributors']}")
    
    # Test message
    simple_test = {
        "roomId": WEBEX_ROOM_ID,
        "text": f"📊 4x2 Grid Test - Escalation #{data['id']}\n\nRow 1: {data['customer']} | {data['version']} | {data['bug_id']} | {data['component']}\nRow 2: {data['severity']} | {data['de_mgr']} | {data['primary_poc']} | {data['contributors']}"
    }
    
    try:
        response = requests.post(url, headers=headers, json=simple_test)
        print(f"\nStatus Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ 4x2 grid test sent successfully!")
            print("📊 Check your Webex space for the 4x2 table layout!")
            return True
        else:
            print(f"❌ Failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

if __name__ == "__main__":
    test_4x2_grid()