#!/usr/bin/env python3
"""
Test if send_escalation_update_to_webex is being called when escalations are edited
"""
import sys
sys.path.append('.')

# Import from your app
from app import app, db, Escalation, send_escalation_update_to_webex
from dotenv import load_dotenv
import os

load_dotenv()

def test_escalation_update():
    """Test sending an escalation update to Webex"""
    print("🧪 Testing Escalation Update Function...\n")
    
    with app.app_context():
        # Get an existing escalation to test with
        escalation = Escalation.query.first()
        
        if not escalation:
            print("❌ No escalations found in database")
            return
        
        print(f"📋 Testing with Escalation #{escalation.id}")
        print(f"   Customer: {escalation.customer}")
        print(f"   Component: {escalation.component_name}")
        print(f"   Severity: {escalation.severity_type}")
        
        # Call the function directly
        print("\n🚀 Calling send_escalation_update_to_webex...")
        try:
            send_escalation_update_to_webex(escalation)
            print("✅ Function completed successfully!")
        except Exception as e:
            print(f"❌ Function failed: {e}")

if __name__ == "__main__":
    test_escalation_update()