import requests

#https://github.com/public-apis/public-apis

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url=api_url)  # send a GET request to the URL

for key, value in response.json().items():  # iterate over the JSON response
    if key =="completed":
        if value == False:
            print(key, ":", "Task is not completed")
        else:
            print(key, ":", "Task is completed")
    print(key, ":", value)  # print each key-value pair
    

#print(dir(response))  # list of all methods in response object
#print(response.status_code)  # print the HTTP status code
#print(response.json())  # print the JSON response

"""
for key, value in response.json().items():  # iterate over the JSON response
  if key =="userId":
        if value in [100, 200, 300]:
            print(key, ":", "User is valid")
            
"""

