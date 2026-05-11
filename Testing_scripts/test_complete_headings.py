#!/usr/bin/env python3
"""
Test complete layout with both section headings
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_complete_layout_with_headings():
    """Test the complete layout with proper section headings"""
    print("🧪 Testing Complete Layout with Section Headings...\n")
    
    WEBEX_BOT_TOKEN = os.getenv("WEBEX_BOT_TOKEN")
    WEBEX_ROOM_ID = os.getenv("WEBEX_ROOM_ID")
    
    if not all([WEBEX_BOT_TOKEN, WEBEX_ROOM_ID]):
        print("❌ Missing Webex credentials")
        return
    
    print("📊 Complete Layout Preview:")
    print("=" * 60)
    print("🚨 Escalation Update - #1")
    print("=" * 60)
    print("\n📋 GENERAL INFORMATION AND TEAMS")
    print("┌─────────────┬─────────────┬─────────────┬─────────────┐")
    print("│  Customer   │   Version   │   Bug ID    │ Component   │")
    print("├─────────────┼─────────────┼─────────────┼─────────────┤")
    print("│   Toyota4   │   17.12.5   │ CSCwr46982  │Client Join  │")
    print("│             │             │             │in SDA       │")
    print("├─────────────┼─────────────┼─────────────┼─────────────┤")
    print("│  Severity   │   DE Mgr    │ Primary PoC │Contributors │")
    print("├─────────────┼─────────────┼─────────────┼─────────────┤")
    print("│     CAP     │   Srihari   │    N/A      │    None     │")
    print("└─────────────┴─────────────┴─────────────┴─────────────┘")
    
    print("\n🔧 ESCALATION DETAILS")
    print("┌─────────────────┬─────────────────┐")
    print("│       SR        │      BEMS       │")
    print("├─────────────────┼─────────────────┤")
    print("│ SR 699613062    │ SR 699613062    │")
    print("├─────────────────┴─────────────────┤")
    print("│    Symptom reported/understood:    │")
    print("├────────────────────────────────────┤")
    print("│ High CPU utilization by WNCDs...  │")
    print("├─────────────────┬─────────────────┤")
    print("│ Upgrade Attempt │  New Version    │")
    print("├─────────────────┼─────────────────┤")
    print("│       No        │      N/A        │")
    print("├─────────────────┴─────────────────┤")
    print("│              Remarks              │")
    print("├────────────────────────────────────┤")
    print("│ [2025-10-29] RCA completed...      │")
    print("└────────────────────────────────────┘")
    
    # Send test message
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {WEBEX_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    
    simple_test = {
        "roomId": WEBEX_ROOM_ID,
        "text": "📊 Complete Layout Test - Two Sections with Headings\n\n📋 GENERAL INFORMATION AND TEAMS\n• Customer: Toyota4\n• Version: 17.12.5\n• Bug ID: CSCwr46982\n• Component: Client Join in SDA\n• Severity: CAP\n• DE Mgr: Srihari\n• Primary PoC: N/A\n• Contributors: None\n\n🔧 ESCALATION DETAILS\n• SR: SR 699613062\n• BEMS: SR 699613062\n• Symptom: High CPU utilization\n• Upgrade Attempt: No\n• Remarks: RCA completed..."
    }
    
    try:
        response = requests.post(url, headers=headers, json=simple_test)
        print(f"\nStatus Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Complete layout with headings sent successfully!")
            print("\n🎯 Your Webex card now shows:")
            print("   1️⃣ Main title: 'Escalation Update - #1'")
            print("   2️⃣ Section 1: '📋 General Information and Teams'")
            print("   3️⃣ Section 2: '🔧 Escalation Details'") 
            print("   4️⃣ Professional grey containers for each section")
            return True
        else:
            print(f"❌ Failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

if __name__ == "__main__":
    test_complete_layout_with_headings()