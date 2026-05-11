#!/usr/bin/env python3
"""
Test two-section layout: General Info + Escalation Details
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_two_section_layout():
    """Test the new two-section layout with grey containers"""
    print("🧪 Testing Two-Section Layout...\n")
    
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
    
    # Test data for both sections
    print("📊 Two-Section Layout Preview:")
    print("\n🔷 GENERAL INFO (Grey Box 1):")
    print("Row 1: Customer    | Version   | Bug ID     | Component")
    print("       Toyota4     | 17.12.5   | CSCwr46982 | Client Join in SDA")
    print("Row 2: Severity    | DE Mgr    | Primary PoC| Contributors")
    print("       CAP         | Hari      | Srihari    | None")
    
    print("\n🔷 ESCALATION DETAILS (Grey Box 2):")
    print("Row 1: Sev Remarks         | Cross Teams | State | Reported On")
    print("       Deploy change...    | Location    | OPEN  | 2025-10-06")
    
    # Send test message
    simple_test = {
        "roomId": WEBEX_ROOM_ID,
        "text": "📊 Two-Section Layout Test\n\n🔷 GENERAL INFO:\nCustomer: Toyota4 | Version: 17.12.5 | Bug ID: CSCwr46982 | Component: Client Join in SDA\nSeverity: CAP | DE Mgr: Hari | Primary PoC: Srihari | Contributors: None\n\n🔷 ESCALATION DETAILS:\nSev Remarks: Deployment change | Cross Teams: Location | State: OPEN | Reported On: 2025-10-06"
    }
    
    try:
        response = requests.post(url, headers=headers, json=simple_test)
        print(f"\nStatus Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Two-section layout test sent successfully!")
            print("📊 Check your Webex space for two grey containers!")
            print("   1️⃣ General Info (8 fields in 4x2 grid)")
            print("   2️⃣ Escalation Details (4 fields in 1x4 grid)")
            return True
        else:
            print(f"❌ Failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

if __name__ == "__main__":
    test_two_section_layout()