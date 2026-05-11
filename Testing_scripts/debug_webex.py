#!/usr/bin/env python3
"""
Debug Webex Integration - Test if messages are being sent properly
"""
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_webex_credentials():
    """Test Webex credentials and basic connectivity"""
    print("🔍 Testing Webex Integration...\n")
    
    # Check environment variables
    WEBEX_BOT_TOKEN = os.getenv("WEBEX_BOT_TOKEN")
    WEBEX_ROOM_ID = os.getenv("WEBEX_ROOM_ID")
    HOST_URL = os.getenv("HOST_URL", "localhost:5000")
    
    print("📋 Environment Variables:")
    print(f"   WEBEX_BOT_TOKEN: {'✅ Set' if WEBEX_BOT_TOKEN else '❌ Missing'}")
    print(f"   WEBEX_ROOM_ID: {'✅ Set' if WEBEX_ROOM_ID else '❌ Missing'}")
    print(f"   HOST_URL: {HOST_URL}")
    
    if not WEBEX_BOT_TOKEN or not WEBEX_ROOM_ID:
        print("\n❌ Missing Webex credentials! Please set them in your .env file")
        return False
    
    print(f"   Token preview: {WEBEX_BOT_TOKEN[:20]}...")
    print(f"   Room ID: {WEBEX_ROOM_ID}")
    
    return WEBEX_BOT_TOKEN, WEBEX_ROOM_ID, HOST_URL

def test_simple_message(token, room_id):
    """Test sending a simple text message first"""
    print("\n🧪 Testing Simple Text Message...")
    
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    simple_message = {
        "roomId": room_id,
        "text": "🧪 Test message from escalation app - simple text"
    }
    
    try:
        response = requests.post(url, headers=headers, json=simple_message)
        print(f"   Status Code: {response.status_code}")
        if response.status_code == 200:
            print("   ✅ Simple text message sent successfully!")
            return True
        else:
            print(f"   ❌ Failed: {response.text}")
            return False
    except Exception as e:
        print(f"   ❌ Exception: {e}")
        return False

def test_table_card(token, room_id, host_url):
    """Test sending the table card format"""
    print("\n🧪 Testing Table Card Format...")
    
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Sample data matching your app format
    data = {
        "id": 999,
        "date": "2025-11-11",
        "customer": "Test Customer",
        "component": "Test Component", 
        "severity": "CAP",
        "remarks": "This is a test escalation card",
        "url": f"http://{host_url}/edit/999"
    }
    
    card = {
        "roomId": room_id,
        "text": f"Escalation Update #{data['id']} - {data['customer']} - {data['component']}",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.2",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": f"Escalation Update - #{data['id']}",
                            "weight": "Bolder",
                            "size": "Medium",
                            "wrap": True
                        },
                        {
                            "type": "ColumnSet",
                            "columns": [
                                {
                                    "type": "Column",
                                    "width": "auto",
                                    "items": [
                                        {
                                            "type": "TextBlock",
                                            "text": "**Date**",
                                            "weight": "Bolder",
                                            "size": "Small"
                                        }
                                    ]
                                },
                                {
                                    "type": "Column",
                                    "width": "auto",
                                    "items": [
                                        {
                                            "type": "TextBlock",
                                            "text": "**Customer**",
                                            "weight": "Bolder",
                                            "size": "Small"
                                        }
                                    ]
                                },
                                {
                                    "type": "Column",
                                    "width": "auto",
                                    "items": [
                                        {
                                            "type": "TextBlock",
                                            "text": "**Component**",
                                            "weight": "Bolder",
                                            "size": "Small"
                                        }
                                    ]
                                },
                                {
                                    "type": "Column",
                                    "width": "auto",
                                    "items": [
                                        {
                                            "type": "TextBlock",
                                            "text": "**Severity**",
                                            "weight": "Bolder",
                                            "size": "Small"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "ColumnSet",
                            "columns": [
                                {
                                    "type": "Column",
                                    "width": "auto",
                                    "items": [
                                        {
                                            "type": "TextBlock",
                                            "text": data["date"],
                                            "size": "Small",
                                            "wrap": True
                                        }
                                    ]
                                },
                                {
                                    "type": "Column",
                                    "width": "auto",
                                    "items": [
                                        {
                                            "type": "TextBlock",
                                            "text": data["customer"],
                                            "size": "Small",
                                            "wrap": True
                                        }
                                    ]
                                },
                                {
                                    "type": "Column",
                                    "width": "auto",
                                    "items": [
                                        {
                                            "type": "TextBlock",
                                            "text": data["component"],
                                            "size": "Small",
                                            "wrap": True
                                        }
                                    ]
                                },
                                {
                                    "type": "Column",
                                    "width": "auto",
                                    "items": [
                                        {
                                            "type": "TextBlock",
                                            "text": data["severity"],
                                            "size": "Small",
                                            "wrap": True
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "TextBlock",
                            "text": f"**Notes:** {data['remarks']}",
                            "wrap": True,
                            "spacing": "Medium"
                        },
                        {
                            "type": "ActionSet",
                            "actions": [
                                {
                                    "type": "Action.OpenUrl",
                                    "title": "📎 View Escalation",
                                    "url": data["url"]
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=card)
        print(f"   Status Code: {response.status_code}")
        if response.status_code == 200:
            print("   ✅ Table card sent successfully!")
            return True
        else:
            print(f"   ❌ Failed: {response.text}")
            return False
    except Exception as e:
        print(f"   ❌ Exception: {e}")
        return False

def main():
    print("🚀 Webex Integration Debugging Tool\n")
    
    # Test credentials
    creds = test_webex_credentials()
    if not creds:
        return
    
    token, room_id, host_url = creds
    
    # Test simple message first
    if test_simple_message(token, room_id):
        # If simple works, test table card
        test_table_card(token, room_id, host_url)
    
    print("\n🏁 Debug test completed!")

if __name__ == "__main__":
    main()