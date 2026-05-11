import requests
from bs4 import BeautifulSoup

try:
    response = requests.get('http://127.0.0.1:5000/statistics')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find contributor analytics section
        contributor_names = soup.find_all('span', class_='contributor-name')
        contributor_counts = soup.find_all('span', class_='contributor-count')
        
        print("Statistics Page - DE Manager Analytics:")
        print("=" * 50)
        
        for i, (name_elem, count_elem) in enumerate(zip(contributor_names, contributor_counts)):
            name = name_elem.get_text().strip()
            count = count_elem.get_text().strip()
            print(f"{i+1}. {name}: {count}")
        
        # Check if hardcoded data is gone
        content = response.text
        hardcoded_names = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Wilson', 'Charlie Brown']
        real_names = ['Hari', 'Gajanan', 'Sthiti', 'Dheeraj']
        
        print("\n" + "=" * 50)
        print("Data Source Verification:")
        print("Hardcoded data present:", any(name in content for name in hardcoded_names))
        print("Real DE Manager data present:", any(name in content for name in real_names))
        
    else:
        print(f"Failed to access statistics page: {response.status_code}")
        
except Exception as e:
    print(f"Error: {e}")