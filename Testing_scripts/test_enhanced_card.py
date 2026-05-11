#!/usr/bin/env python3
"""
Test enhanced card format that definitely works on both mobile and desktop
"""
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_enhanced_card_format():
    """Test an enhanced card format that works universally"""
    print("🧪 Testing Enhanced Card Format...\n")
    
    # Get credentials
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
    
    # Enhanced card format - very compatible
    data = {
        "id": 999,
        "date": "2025-11-11",
        "customer": "Test Customer Enhanced",
        "component": "Test Component Enhanced", 
        "severity": "CAP",
        "remarks": "This is an enhanced test card format that should work perfectly on both mobile and desktop",
        "url": f"http://{HOST_URL}/edit/999"
    }
    
    enhanced_card = {
        "roomId": WEBEX_ROOM_ID,
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
                            "text": f"🚨 Escalation Update - #{data['id']}",
                            "weight": "Bolder",
                            "size": "Medium",
                            "wrap": True,
                            "color": "Attention"
                        },
                        {
                            "type": "Container",
                            "style": "emphasis",
                            "items": [
                                {
                                    "type": "FactSet",
                                    "facts": [
                                        {
                                            "title": "📅 Date:",
                                            "value": data["date"]
                                        },
                                        {
                                            "title": "🏢 Customer:",
                                            "value": data["customer"]
                                        },
                                        {
                                            "title": "⚙️ Component:",
                                            "value": data["component"]
                                        },
                                        {
                                            "title": "🔴 Severity:",
                                            "value": data["severity"]
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "TextBlock",
                            "text": f"**📝 Notes:**",
                            "weight": "Bolder",
                            "spacing": "Medium"
                        },
                        {
                            "type": "TextBlock", 
                            "text": data['remarks'],
                            "wrap": True,
                            "spacing": "Small"
                        },
                        {
                            "type": "ActionSet",
                            "actions": [
                                {
                                    "type": "Action.OpenUrl",
                                    "title": "📎 View Escalation Details",
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
        response = requests.post(url, headers=headers, json=enhanced_card)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Enhanced card sent successfully!")
            print("📱 This format should work perfectly on both mobile and desktop!")
            return True
        else:
            print(f"❌ Failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

if __name__ == "__main__":
    test_enhanced_card_format()