#!/usr/bin/env python3
"""
Test clean table format that matches the Concur Approvals style from image 2
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_clean_table_format():
    """Test clean table format matching image 2 style"""
    print("🧪 Testing Clean Table Format (Image 2 Style)...\n")
    
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
    
    # Test data
    data = {
        "id": 123,
        "date": "2025-11-11",
        "customer": "Test Customer Corp",
        "component": "Network Component XYZ", 
        "severity": "CAP",
        "remarks": "This is a test escalation with clean table format matching the Concur Approvals style from image 2.",
        "url": f"http://{HOST_URL}/edit/123"
    }
    
    # Clean table format matching image 2
    clean_table_card = {
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
                            "text": f"Escalation Update - #{data['id']}",
                            "weight": "Bolder",
                            "size": "Medium",
                            "wrap": True
                        },
                        {
                            "type": "Container",
                            "style": "emphasis",
                            "items": [
                                {
                                    "type": "ColumnSet",
                                    "columns": [
                                        {
                                            "type": "Column",
                                            "width": "25%",
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
                                            "width": "25%",
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
                                            "width": "25%", 
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
                                            "width": "25%",
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
                                            "width": "25%",
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
                                            "width": "25%", 
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
                                            "width": "25%",
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
                                            "width": "25%",
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
        response = requests.post(url, headers=headers, json=clean_table_card)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Clean table format sent successfully!")
            print("📊 This should now match the style from image 2!")
            return True
        else:
            print(f"❌ Failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

if __name__ == "__main__":
    test_clean_table_format()