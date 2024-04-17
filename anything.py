import requests
import json

def send_message(message):
    # Define the API endpoint URL
    url = 'http://localhost:3001/api/v1/workspace/mia/chat'

    # Define the request headers
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer RQ1VC5T-XXXXXXX-XXXXXXX-XXXXXXX',
        'Content-Type': 'application/json'
    }

    # Define the request body for the new message
    data = {
        "message": message,
        "mode": "query"
    }

    # Convert the data dictionary to JSON format
    data_json = json.dumps(data)

    try:
        # Send the POST request
        response = requests.post(url, headers=headers, data=data_json)
        
        # Parse the response JSON data
        response_data = response.json()
        
        # Get the bot's response
        bot_response = response_data.get("textResponse")
        
        # Print the bot's response
        if bot_response:
            print(f"Bot: {bot_response}")
        
        # Prompt for a new message
        new_message = input("You: ")
        
        # Return the new message
        return new_message

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Initial message
    message = input("You: ")
    
    while message.lower() != "exit":
        # Send the user's message and get a new message
        message = send_message(message)

    print("Chat ended.")
