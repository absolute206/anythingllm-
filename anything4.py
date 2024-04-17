import requests
import json
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract the main content from the webpage
            content = soup.find('body').text  # Modify this to extract specific content
            
            return content
            
        else:
            print(f"Failed to retrieve website content: {response.text}")
            return None

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def upload_link(link, auth_token):
    # Define the API endpoint URL for uploading the link
    url = 'http://localhost:3001/api/v1/document/upload-link'

    # Define the request headers with the provided authorization token
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }

    # Define the request body
    data = {
        "link": link
    }

    try:
        # Send the POST request to upload the link
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Link uploaded successfully.")
            return True
        else:
            print(f"Failed to upload link: {response.text}")
            return False
            
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def embed_content(auth_token, document_path):
    # Define the API endpoint URL with the slug "mia" for embedding
    url = f'http://localhost:3001/api/v1/workspace/mia/update-embeddings'

    # Define the request headers with the provided authorization token
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }

    # Define the request body
    data = {
        "adds": [
            document_path
        ],
        "deletes": []
    }

    try:
        # Send the POST request to embed the content
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Content embedded successfully.")
        else:
            print(f"Failed to embed content: {response.text}")
            
    except requests.RequestException as e:
        print(f"Request failed: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt user for website URL
    website_url = input("Enter the website URL to scrape: ")
    
    # Provide the authentication token
    auth_token = 'RQ1VC5T-8R3MXP3-KNXRHRY-22VEPHC'
    
    # Call the upload_link function to upload the website URL
    if upload_link(website_url, auth_token):
        # Call the embed_content function to embed the uploaded content
        document_path = "custom-documents/scraped_content.txt-hash.json"  # Replace with the actual path to the uploaded document
        embed_content(auth_token, document_path)
