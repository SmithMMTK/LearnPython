## Call API server and get JSON data

import requests

# Call the API server
response = requests.get('http://ifconfig.co/json')

# Check if the response is successful
if response.status_code == 200:
    # Get the JSON data
    data = response.json()
    
    # Print the JSON data
    print(data)
else:
    # Print an error message
    print('An error occurred while calling the API server.')
