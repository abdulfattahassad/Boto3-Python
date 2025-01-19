# 1- Python Module contain mluple pyhon files OR file - these file contain functions, class which are
# template  , objects, variable 
# 2- requests  is Module
# 3- Response is Class  in requests module - which template contain different settings like text, json , status-code
# when you create  response=request.get ==> response will be object of Response class in order to 
# to hold the reponse result like status code, jason 


# example:
# def request(method, url, **kwargs):
    # Prepare the request, handle headers, parameters, etc.
#   response = send_request(method, url, kwargs)
#    return response

import requests
from pprint import pprint
pprint(dir(requests.Response))
# print(dir(requests.Response))


# what is HTTP request looks like:
#GET /path HTTP/1.1
#Host: www.example.com
#User-Agent: Python/3.9 requests/2.25.1
#Accept: application/json
#Authorization: Bearer your-api-key-here
#Content-Type: application/json
# Connection: keep-alive

# to send custome API header :
import requests

# Define the URL and custom headers
url = "https://api.example.com/data"
headers = {
    "User-Agent": "MyApp/1.0",  # Custom User-Agent string
    "Authorization": "Bearer your-api-key",  # Bearer Token for authorization
    "Content-Type": "application/json",  # Indicating JSON format
    "Accept": "application/json",  # Accepting JSON response
}

# Sending a GET request with custom headers
response = requests.get(url, headers=headers)

# Output the response status code and JSON data
print(response.status_code)  # E.g., 200
print(response.json())  # Parsed JSON content from the response


#### Authentication and Authorizaion : 
#API Key in Custom Header (e.g., "Authorization" or "X-API-Key"):

# Some APIs might use custom headers like "X-API-Key", "X-Authorization", or others instead of "X-Auth-Token".

#import requests

# API endpoint
#url = "https://api.example.com/protected-data"

# Bearer token for authentication
#token = "your-api-token-here"

# Set the Authorization header
#headers = {
#    "Content-Type": "application/json",  # Content type of the request
#}

# Send the GET request
#response = requests.get(url, headers=headers)

# Print the response status and data
#print(response.status_code)
#print(response.json())
