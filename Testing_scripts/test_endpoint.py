import requests
import json

try:
    # Test the statistics endpoint
    response = requests.get('http://127.0.0.1:5000/statistics')
    if response.status_code == 200:
        # Look for contributor data in the HTML
        html_content = response.text
        
        # Check if there are contributor sections
        if 'contributor-name' in html_content:
            print("Found contributor data in HTML")
            
            # Extract lines containing contributor names
            lines = html_content.split('\n')
            contributor_lines = []
            for i, line in enumerate(lines):
                if 'contributor-name' in line:
                    # Get the context around contributor lines
                    start = max(0, i-2)
                    end = min(len(lines), i+3)
                    contributor_lines.extend(lines[start:end])
            
            print("Contributor HTML sections:")
            for line in contributor_lines[:20]:  # Show first 20 lines
                print(line.strip())
        else:
            print("No contributor data found in HTML")
    else:
        print(f"Failed to get statistics page: {response.status_code}")
        
except Exception as e:
    print(f"Error testing statistics endpoint: {e}")