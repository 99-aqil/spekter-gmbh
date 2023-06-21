import requests

# Define the API endpoint URL
url = 'http://localhost:8000/analyze/'

# Define the text to be analyzed
text = 'happy'

# Create the request payload
payload = {
    'text': text
}

# Send the POST request to the API
response = requests.post(url, json=payload)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    print(response_data)
    
    # Retrieve the sentiment from the response
    # sentiment = response_data['sentiment']
    
    # Print the sentiment analysis result
    # print(f'Sentiment: {sentiment}')
else:
    print('Error occurred while making the request.')
