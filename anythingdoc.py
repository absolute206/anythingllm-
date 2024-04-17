import requests
import json
import sys

url = 'http://localhost:3001/api/v1/documents'
headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer RQ1VC5T-XXXXXXX-XXXXXXX-XXXXXXX'
}

try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        
        if 'documents' in data and isinstance(data['documents'], list):
            for document in data['documents']:
                title = document['title']
                published_date = document['published']
                
                print("Title:", title, "Published Date:", published_date)
        else:
            print("Data structure does not contain 'documents' key or its value is not a list.")
    else:
        print("Request failed with status code", response.status_code)
except Exception as e:
    print(str(e), file=sys.stderr)
