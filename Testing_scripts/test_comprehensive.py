#!/usr/bin/env python3
"""
Test comprehensive table format with all requested fields
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_comprehensive_table():
    """Test comprehensive table with all fields as requested"""
    print("🧪 Testing Comprehensive Table Format...\n")
    
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
    
    # Comprehensive test data matching your specification
    data = {
        "id": 456,
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
        "remarks": "This is a comprehensive test of all escalation fields in table format.",
        "url": f"http://{HOST_URL}/edit/456"
    }
    
    print("📋 Test Data:")
    print(f"   Customer: {data['customer']}")
    print(f"   Version: {data['version']}")
    print(f"   Bug ID: {data['bug_id']}")
    print(f"   Component: {data['component']}")
    print(f"   Severity: {data['severity']}")
    print(f"   Sev Remarks: {data['severity_remarks']}")
    print(f"   DE Mgr: {data['de_mgr']}")
    print(f"   Primary PoC: {data['primary_poc']}")
    print(f"   Contributors: {data['contributors']}")
    print(f"   Cross Teams: {data['cross_teams']}")
    
    # Test message
    simple_test = {
        "roomId": WEBEX_ROOM_ID,
        "text": f"📊 Comprehensive Escalation Test - All Fields\n\nCustomer: {data['customer']}\nVersion: {data['version']}\nBug ID: {data['bug_id']}\nComponent: {data['component']}\nSeverity: {data['severity']}\nSev Remarks: {data['severity_remarks']}\nDE Mgr: {data['de_mgr']}\nPrimary PoC: {data['primary_poc']}\nContributors: {data['contributors']}\nCross Teams: {data['cross_teams']}"
    }
    
    try:
        response = requests.post(url, headers=headers, json=simple_test)
        print(f"\nStatus Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Comprehensive test data sent successfully!")
            print("📊 Check your Webex space for the complete field layout!")
            return True
        else:
            print(f"❌ Failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

if __name__ == "__main__":
    test_comprehensive_table()