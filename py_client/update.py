import requests

endpoint = "http://127.0.0.1:8000/products/1"

data = {
    "name": "updated Hello world 4",
    "description": "Updated Description 4",
    "price": 10.00,
}


get_response = requests.put(endpoint, json=data)

print(get_response.json())
