import requests
import json

def main():
    # Prompt user for a URL
    url = input("Please enter the URL to be scraped: ")

    # API endpoint URL
    api_endpoint = "http://localhost:3001/api/v1/document/upload-link"

    # Authorization token
    authorization_token = "Bearer RQ1VC5T-XXXXXXX-XXXXXXX-XXXXXXX"

    # Headers
    headers = {
        "accept": "application/json",
        "Authorization": authorization_token,
        "Content-Type": "application/json"
    }

    # Request body
    payload = {
        "link": url
    }

    try:
        # Send POST request
        response = requests.post(api_endpoint, headers=headers, data=json.dumps(payload))
        
        # Check if the request was successful
        if response.status_code == 200:
            print("URL has been successfully uploaded for scraping.")
        else:
            print(f"Failed to upload URL. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
