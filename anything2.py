import requests
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

def upload_file(content, auth_token):
    # Define the API endpoint URL
    url = 'http://localhost:3001/api/v1/document/upload'

    # Define the request headers
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    # Prepare the content as a file-like object
    file_content = content.encode('utf-8')
    
    files = {'file': ('scraped_content.txt', file_content, 'text/plain')}
    
    try:
        # Send the POST request
        response = requests.post(url, headers=headers, files=files)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("File uploaded successfully.")
        else:
            print(f"Failed to upload file: {response.text}")
            
    except requests.RequestException as e:
        print(f"Request failed: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt user for website URL and authentication token
    website_url = input("Enter the website URL to scrape: ")
    auth_token = input("Enter the Authorization token: ")
    
    # Call the scrape_website function to scrape the website content
    website_content = scrape_website(website_url)
    
    if website_content:
        # Call the upload_file function to upload the scraped content
        upload_file(website_content, auth_token)
