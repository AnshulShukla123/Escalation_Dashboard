#!/usr/bin/env python3
"""
Test updated escalation details with SR, BEMS, Symptom, Upgrade Attempt, and Remarks
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_updated_escalation_details():
    """Test the updated escalation details section"""
    print("🧪 Testing Updated Escalation Details Section...\n")
    
    WEBEX_BOT_TOKEN = os.getenv("WEBEX_BOT_TOKEN")
    WEBEX_ROOM_ID = os.getenv("WEBEX_ROOM_ID")
    HOST_URL = os.getenv("HOST_URL", "localhost:5000")
    
    if not all([WEBEX_BOT_TOKEN, WEBEX_ROOM_ID]):
        print("❌ Missing Webex credentials")
        return
    
    # Display the new structure
    print("📊 Updated Two-Section Layout:")
    print("\n🔷 GENERAL INFO (Grey Box 1 - 4x2 grid):")
    print("Row 1: Customer    | Version   | Bug ID     | Component")
    print("       Toyota4     | 17.12.5   | CSCwr46982 | Client Join in SDA")
    print("Row 2: Severity    | DE Mgr    | Primary PoC| Contributors")
    print("       CAP         | Hari      | Srihari    | None")
    
    print("\n🔷 ESCALATION DETAILS (Grey Box 2 - 4 rows):")
    print("Row 1: SR          | BEMS")
    print("       SR 699613062| SR 699613062")
    print("Row 2: Symptom reported/understood:")
    print("       High CPU utilization by the WNCDs...")
    print("Row 3: Any upgrade attempt and new version:")
    print("       No")
    print("Row 4: Remarks:")
    print("       We have RCAed this issue...")
    
    # Send test message
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {WEBEX_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    
    test_message = {
        "roomId": WEBEX_ROOM_ID,
        "text": """📊 Updated Escalation Details Layout Test

🔷 GENERAL INFO:
Customer: Toyota4 | Version: 17.12.5 | Bug ID: CSCwr46982 | Component: Client Join in SDA
Severity: CAP | DE Mgr: Hari | Primary PoC: Srihari | Contributors: None

🔷 ESCALATION DETAILS:
SR: SR 699613062 | BEMS: SR 699613062
Symptom: High CPU utilization by the WNCDs when clients are joining/roaming at a 50 CPS
Upgrade Attempt: No
Remarks: We have RCAed this issue. Based on the archive analysis..."""
    }
    
    try:
        response = requests.post(url, headers=headers, json=test_message)
        print(f"\nStatus Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Updated escalation details test sent successfully!")
            print("📊 Check your Webex space for the new layout!")
            print("   1️⃣ General Info: 8 fields in 4x2 grid")
            print("   2️⃣ Escalation Details: SR, BEMS, Symptom, Upgrade Attempt, Remarks")
            return True
        else:
            print(f"❌ Failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

if __name__ == "__main__":
    test_updated_escalation_details()