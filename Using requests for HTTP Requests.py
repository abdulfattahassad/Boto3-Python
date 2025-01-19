# Requests Module  if exist , please install it via :pip3 install requests

import requests
from pprint import pprint  

url = 'https://jsonplaceholder.typicode.com/posts'
# GET request
response = requests.get(url)

# as we explain that response is object of Response Class in requests module  and have different items
# with values so if you want to access these value you can 
pprint(f"this is  response {response.status_code}")

#pprint(response.json())
# POST request
#data = {'key': 'value'}
#response = requests.post('https://api.example.com/data', json=data)
#print(response.json())


### Json=data : send the data as  : The body will contain the data as JSON, such as {"key": "value"}.
## data = data : The body will contain the data as url encoded, such as key = value 
#In short, using data=data with requests.post() sends the data as form data 
#(application/x-www-form-urlencoded),
# while using json=data sends the data as JSON (application/json). 
# The choice of which to use depends on how the server expects to receive the data. 
# If the server expects form data (like a standard web form submission), you use data. 
# If the server expects JSON (like most modern APIs), you use json.

# Exmple: name=John+Doe&age=30
#The server would parse the data and map:

#name -> John Doe
#age -> 30
#Use Case: HTML Forms
#When you submit a form in an HTML page without using JavaScript or other advanced methods, the browser typically sends the data in application/x-www-form-urlencoded format. Here’s an example:

#html
#Copy
#<form action="https://example.com/submit" method="POST">
#  <input type="text" name="name" value="John Doe">
#  <input type="number" name="age" value="30">
#  <button type="submit">Submit</button>
#</form>
#When this form is submitted, the browser sends the following data:

# name=John+Doe&age=30