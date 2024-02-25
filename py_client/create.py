import requests

endpoint = "http://127.0.0.1:8000/products/"

data = {
    "name": "new ",
    "description": "Hello World",
    "price": 20.28,
    "image_url": "",
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())
