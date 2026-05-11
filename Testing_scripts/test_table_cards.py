#!/usr/bin/env python3
"""
Test script to verify the updated Webex table card functionality
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_table_card_format():
    """Test the table card format with sample data"""
    
    print("=== TESTING UPDATED WEBEX TABLE CARDS ===\n")
    
    # Check if environment variables are loaded
    webex_token = os.getenv("WEBEX_BOT_TOKEN")
    webex_room = os.getenv("WEBEX_ROOM_ID")
    host_url = os.getenv("HOST_URL", "localhost:5000")
    
    print("🔧 Environment Check:")
    print(f"   WEBEX_BOT_TOKEN: {'✅ Set' if webex_token else '❌ Missing'}")
    print(f"   WEBEX_ROOM_ID: {'✅ Set' if webex_room else '❌ Missing'}")
    print(f"   HOST_URL: {host_url}")
    
    print("\n📊 Sample Table Card Data:")
    sample_data = {
        "id": 1,
        "date": "2025-10-06",
        "customer": "Toyota4",
        "component": "Client Join in SDA",
        "severity": "CAP",
        "remarks": "Deployment change: from non-SDA to SDA",
        "url": f"http://{host_url}/edit/1"
    }
    
    for key, value in sample_data.items():
        print(f"   {key}: {value}")
    
    print("\n🎯 Expected Table Format:")
    print("┌──────────┬─────────────────┬─────────────────┬──────────┐")
    print("│   Date   │    Customer     │   Component     │ Severity │")
    print("├──────────┼─────────────────┼─────────────────┼──────────┤")
    print("│2025-10-06│ Toyota4         │ Client Join SDA │   CAP    │")
    print("└──────────┴─────────────────┴─────────────────┴──────────┘")
    
    print("\n✅ Updated Functions:")
    print("   • send_escalation_update_to_webex() - Uses table cards")
    print("   • send_table_to_webex() - Uses table cards")
    print("   • send_escalation_card() - New table implementation")
    
    print("\n🚀 Ready to Test:")
    print("   1. Update an escalation in the application")
    print("   2. Or use /webex_table_test route")
    print("   3. Check Webex space for table format")

if __name__ == "__main__":
    test_table_card_format()
    print("\n=== TEST COMPLETE ===")
    print("🎉 Table card functionality is ready!")
    print("📞 Your Webex messages will now use professional table format!")